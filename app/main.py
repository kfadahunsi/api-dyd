from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import redis.asyncio as aioredis
from contextlib import asynccontextmanager
import httpx
import os

from draftcup import produce_league_table, get_semis, get_semi_results, get_finals, get_winner, fixture_path, get_fixtures

from apifunctions import get_gw_info, get_manager_data, get_team_lists, make_league_table, base_url

from config import entry_ids, ALLOWED_ORIGINS, REDIS_URL, SEASON, full_team_ids


async def lifespan(app: FastAPI):
    #startup
    redis = aioredis.from_url(REDIS_URL)
    app.state.redis = redis #kept on state so the health check can ping it
    FastAPICache.init(RedisBackend(redis), prefix="myapp-cache")
    yield
    # Shutdown (anything after yield runs when the app stops)

app = FastAPI(lifespan=lifespan)

#allows you to fetch your data from a browswer thats on your same network. Cross Oigin Requests
#previously, allow credentials was true, but this was changed to false due to errors, if credentials eg auth and cookies are needed, set to tru and then change allow all origins and specify the specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    """
    liveness check, for railway and for a quick "is the api even up" from a browser.
    deliberately does no i/o and is NOT cached: it has to keep answering when redis
    or the fpl api are down, otherwise it can't tell you that they are down.
    """
    return {"status": "ok", "season": SEASON}


@app.get("/health/detailed")
async def health_detailed(response: Response):
    """
    readiness check. covers the things that have actually taken this api offline
    before: redis, the upstream fpl draft api, and the season data files on disk
    drifting out of step with the ids in config.

    not cached either, for the same reason as above, so the upstream call is given
    a short timeout to stop this endpoint hanging.
    """
    checks = {}

    #redis only backs the response cache, and fastapi-cache falls through to the real
    #function when it can't reach it. so an outage here means slower responses and more
    #load on the fpl api rather than downtime, which is why it's a warning below and
    #not a failure - a 503 would have railway restart a container that is serving fine
    try:
        await app.state.redis.ping()
        checks["redis"] = {"ok": True}
    except Exception as e:
        checks["redis"] = {"ok": False, "error": f"{type(e).__name__}: {e}"}

    #cheapest upstream endpoint, the same one get_gw_info() uses
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            upstream = await client.get(base_url + "game")
        checks["fpl_api"] = {"ok": upstream.status_code == 200, "status_code": upstream.status_code}
    except Exception as e:
        checks["fpl_api"] = {"ok": False, "error": f"{type(e).__name__}: {e}"}

    #this is the check that would have caught the /cup_table 500: after a team was
    #renamed in config the fixture file still held the old name and every request
    #died on a bare KeyError
    try:
        fixtures = get_fixtures()
        named = {name for fixture in fixtures for name in (fixture["home"], fixture["away"])}
        unknown = sorted(named - set(full_team_ids))
        checks["fixtures"] = {
            "ok": not unknown,
            "file": os.path.basename(fixture_path),
            "count": len(fixtures),
            "unknown_teams": unknown,
        }
    except Exception as e:
        checks["fixtures"] = {"ok": False, "file": os.path.basename(fixture_path), "error": f"{type(e).__name__}: {e}"}

    #reported because a missing origin makes the site look completely dead from a
    #browser while every endpoint still happily returns 200 to curl
    checks["allowed_origins"] = ALLOWED_ORIGINS

    #only the checks that actually stop the api serving real data get to fail the
    #endpoint. everything else is reported but still answers 200
    CRITICAL = ("fpl_api", "fixtures")
    failing = [name for name in CRITICAL if not checks[name]["ok"]]
    warnings = [
        name for name, result in checks.items()
        if isinstance(result, dict) and not result["ok"] and name not in CRITICAL
    ]

    if failing:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        overall = "unhealthy"
    elif warnings:
        overall = "degraded"
    else:
        overall = "ok"

    return {
        "status": overall,
        "season": SEASON,
        "failing": failing,
        "warnings": warnings,
        "checks": checks,
    }


@app.get("/league_table")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def league_table():
    data = await make_league_table()
    return data
    
    

@app.get("/cup_table")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
def cup_table():
    return produce_league_table()

@app.get("/fixtures")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
def fixtures():
    return get_fixtures()

@app.get("/gw_status")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def gw_status():
    data = await get_gw_info()
    return data

@app.get("/home_stats")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def home_stats():
    manager_gw_stats = []
    for key in entry_ids.keys():
        data = await get_manager_data(entry_ids[key])
        if data:
            manager_gw_stats.append(data["entry"])
    sorted_stats = sorted(manager_gw_stats, key=lambda stat: stat["event_points"], reverse=True)
    return sorted_stats

        
@app.get("/league_teams")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def league_teams():
    gw_info = await get_gw_info()
    gw = gw_info["current_event"]
    return await get_team_lists(gw)

@app.get("/semi_finals")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def semi_finals():
    semis = await get_semis()
    return semis

@app.get("/semi_results")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def semi_results():
    semi_results = await get_semi_results()
    return semi_results

@app.get("/finals")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def finals():
    finals = await get_finals()
    return finals

@app.get("/winner")
@cache(expire=300) #caching so it makes a new api acall after 300s (5 mins)
async def winner():
    winner = await get_winner()
    return winner