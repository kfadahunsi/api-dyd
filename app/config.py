import os

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")


#bump this once per season. every data file path is derived from it, so the
#cup fixtures, knockout and table history files must be named to match. do not bump until you have created the fixture file.
SEASON = "26_27"

# 26/27 season — IDs from GET /league/{league_id}/details
# entry_id: used for /entry/{id}/public and squads (GW picks)
# id (league_entry): used in standings as league_entry
entry_ids = {
        "ASA": 1097,
        "SSFC": 96198,
        "DTF": 96968,
        "DVFF": 195192,
        "SLS": 213720,
        "MMUFC": 244365,
    }

league_id = 521

team_ids = {
        "ASA": 1097,
        "SSFC": 96458,
        "DTF": 97236,
        "DVFF": 196222,
        "SLS": 214991,
        "MMUFC": 246326,
}

# Keys must match FPL entry_name — they are the labels on the league table
full_team_ids = {
    "Amassing Silvaware": 1097,
    "Super Slimey Fütbol": 96458,
    "Darwin’s Theory": 97236,
    "De Vrij Fish Futbol": 196222,
    "Saint Laurent Slot": 214991,
    "Maatsen Margiela Utd": 246326,
}









ifc_team_id = 324714
ifc_league_id = 63351


#the restricted fpl endpoints need a logged in session. the tokens that used to
#live here were committed to a public repo and are long expired, so they have been
#removed. if a restricted endpoint is ever needed again, read the token from the
#environment (FPL_ACCESS_TOKEN in .env.local locally, a railway variable in prod)
#and build the headers at call time - never commit them. see the note below for
#how to regenerate them.

"""
Log in to the fpl website in browser
Open the inspection console 
Click on the network tab, you will see a similar table to the one below:
Navigate to any page on the fpl site eg “pick team” which should trigger the table to be populated
Right click on one of the rows which is an api call, eg the highlighted one in the picture above.
Click on copy value > copy as cURL (POSIX)
Paste the copied info to this site https://curlconverter.com/
This will generate the headers and cookies you need to put into any request that requires them
"""

