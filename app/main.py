from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import redis.asyncio as aioredis
from contextlib import asynccontextmanager

from draftcup import produce_league_table, get_semis, get_semi_results, get_finals, get_winner

from apifunctions import get_gw_info, get_manager_data, get_team_lists, make_league_table

from helper_functions import load_json
from config import entry_ids, ALLOWED_ORIGINS, REDIS_URL

import os


async def lifespan(app: FastAPI):
    #startup
    redis = aioredis.from_url(REDIS_URL)
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

@app.get("/debug")
def debug():
    return {
        "allowed_origins": os.getenv("ALLOWED_ORIGINS"),
        "test": os.getenv("TEST_VAR")
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
    file_path = r"C:\Users\Kevwe Fadahunsi\Documents\Coding\React Portfolio\api-dyd\data\cup fixtures\25_26.json"
    fixtures = load_json(file_path)
    return fixtures

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