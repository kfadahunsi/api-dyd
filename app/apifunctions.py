import requests, json
from pprint import pprint
import httpx
import asyncio
from config import cookies, headers, entry_ids, league_id, team_ids, full_team_ids


base_url = "https://draft.premierleague.com/api/"


#note, you should never exit(0) for code being used in an api
#the entry set is the league id
"""
This is section 1, the functions here, make calls to the api and return the data from a successful response otherwise,
an error message
"""

async def get_manager_data(entry_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"entry/{entry_id}/public")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    


async def get_gw_info():
    """
    returns the current gw number, whether the gw has been completed, its processing status, 
    whether we are still able to trade, whether waivers have been processed. 
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"game")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    
    
async def get_all_data():
    """
    returns multiple dictionaries.

    elements - a list of player dictionaries containing information about the players
    element type - list of dictionaries of all element types and relevant info. type 1- goal keeper, 2-defender, 3- midfielder, 4- forward
    element stats - list  of dicts of all the different stats relating to a player and whether they are match stats eg red card or not, eg draft rank
    events - has the current gw number as a property, then has a list of dicts of each gw and its info eg number, finished, trades time, waivers time etc
    fixtures - dict that holds the current gws fixtures as a list of dicts for each fixture
    settings - holds info on the league settings that were done at season start
    teams - list of dicts for each premier league team including an ID, name, code etc
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"bootstrap-static")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    
async def get_league_details(league_id):
    """
    returns a dictionary of dictionaries:
    league - information about the league eg no of entrants, draft date etc
    league entries - dict containing all the members in the league and their information 
    standings - list of dicts for each player and their current league position
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"league/{league_id}/details") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


async def get_player_status():
    """
    a dictionary of one dictionary
    element status - list of dictionaries containing information about players and whether they are owned, or have been traded
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"league/{league_id}/element-status") # true or false on whether a player has been in an accepted trade
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


async def get_trades():
    """
    dictionary with one item "trades" which contains a list of dictionaries of 
    all the trades that have occurred within the league and their relevant info
    eg between which parties, which players were traded
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"draft/league/{league_id}/trades") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

async def get_transactions(team_id):
    """
    requires special access.
    returns all the transactions made for the specified ID.
    ensure to add headers and payload if necessary 
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"draft/entry/{team_id}/transactions", headers=headers, cookies=cookies) #unable to check because of team ID
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


async def get_status():
    """
    returns a dictionary containing dictionaries for each match day of the current gw
    matchday dictionaries contain whether bonus points have been added, the date of the match day, the gw, 
    and whether the league has been updated.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"pl/event-status") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

async def get_player_gw_stats(gw):
    """
    returns a dict of every player in the game and their stats for selected gw
    elements - player dictionaries and their stats
    fixtures - each fixture and its corrsponding stats
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"event/{gw}/live") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


async def get_team(team_id):
    """
    requires special access.
    returns the currnt team for the specified ID 
    ensure to add headers and payload if necessary
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"entry/{team_id}/my-team") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

async def get_choices():
    """
    dictionary with 3 entries
    choices - list of dictionaries containing the draft day order and information from round 1 to 15
    idle - empty list?
    element status - complete player object list. 800+ players. contains ID, 
       whether accepted in a trade, ownerID, and status (owned/available)
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"draft/{league_id}/choices") #unclear what the information is
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None



async def get_watchlist(team_id):
    """
    requires special access.
    watchlist
    ensure to add headers and payload if necessary
    """
    pass
    #async with httpx.AsyncClient() as client:
        #response = client.get(base_url + f"watchlist/{team_id}" , headers=headers, cookies=cookies) #unable to check because of team ID

async def get_team_gw(entry_id, gw):
    """
    dictionary with three keys, entries, picks and subs.
    entries - empty dict
    picks - contains a list of player objects with info about the specified team's players eg.
    player id, position, multiplier, is captain, is vice captain
    subs - list of dicts containing which player was subbed in, subbed out and what gw this is for. 
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"entry/{entry_id}/event/{gw}") 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None




async def get_dynamic_info():
    """
    returns dictionary with entries 'player', 'entries', 'leagues', 'time', 'active'. 
    all entries empty. 
    when logged in with headers and cookies:
    player - players email, name and other personal info
    leagues - all the leagues they are in, including mocks
    entries - list of every league you entered in order, including mocks 
    active - which league is currently selected, including the watchlist
    time - the time as a raw number
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url + f"bootstrap-dynamic" , headers=headers, cookies=cookies) # nothing useful. just provides datetime
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


#put any of the functions below to see their output
#data = get_player_gw_stats(31)
#pprint(data["elements"])


"""
This is section 2, the functions here, manipulate the data returned from the successful responses into useable pieces.
"""

def get_specific_player_info(player_id: str, info:str, all_data):
    data = all_data
    players = data["elements"]
    teams = data["teams"]
    positions = data["element_types"]
    

    if info == "name":
     for player in players:
        if player["id"] == player_id:
            return player["web_name"]
        
    elif info == "team":
     for player in players:
        if player["id"] == player_id:
            team_num = player["team"]
            for team in teams:
                if team["id"] == team_num:
                    return team["short_name"]
    
    elif info == "position":
        for player in players:
            if player["id"] == player_id:
                position_num = player["element_type"]
                for player_type in positions:
                    if player_type["id"] == position_num:    
                        return player_type["singular_name_short"]
     

    
async def make_team_lists(entry_ids, gw: int, all_data, gw_stats):
    """
    traverses throught each key and value from the entry ids dict. 
    creates a team list for each one. 
    gets the data associated with each one. 
    extracts the data into lineup, subs .
    
    using gw, gets the player stats for the gw
    extracts just the list of players which is relevant.
    
    traverses each player in a lineup and makes a new dict (player_dict) for each one.
    gets the  player name, team, and position for each one.
    
    traverses the player stats dictionary and matches its id with an id from the player lineup.
    when the ids match, it fills player_dict with the relevant information for each player from both the lineup information and the player stats. 
    
    necessary info - player name, team name, player position, general information, points explained, stats.
    
    player dict is appended to league_teams_list
    
    league_teams_list is added to the leagu_teams dict with the club acronym eg ASA as the key. 
    
    """
    
    league_teams = {}
    player_stats = gw_stats["elements"]
    
    for team, entry_id in entry_ids.items():
        league_teams_list = []
        data = await get_team_gw(entry_id, gw)
        lineup = data["picks"]
        subs = data["subs"]
        for starter in lineup:
            player_dict = {}
            player_name = get_specific_player_info(starter["element"], "name", all_data)
            player_team = get_specific_player_info(starter["element"], "team", all_data)
            player_position = get_specific_player_info(starter["element"], "position", all_data)
            
            for element_id, player in player_stats.items():
                if int(element_id) == starter["element"]:
                    player_dict["basic"] = dict(name= player_name, team=player_team, position=player_position)
                    player_dict["general"] = starter
                    player_dict["explained"] = player["explain"]
                    player_dict["stats"]    = player["stats"]
                    
            #pprint(player_dict)  
            league_teams_list.append(player_dict)
        league_teams[team] = league_teams_list
    return league_teams
                        
                    
                        #print(get_specific_player_info(starter["element"], "name"))
                        #pprint(player)

            
async def get_team_lists(gw: int):
    all_data = await get_all_data()
    gw_stats = await get_player_gw_stats(gw)
    return await make_team_lists(entry_ids, gw, all_data, gw_stats)

async def make_league_table():
    league_details = await get_league_details(league_id)
    standings = league_details["standings"]
    league_table ={}
    
    for item in standings:
        for team_name, team_id in full_team_ids.items():
            if team_id == item["league_entry"]:
                league_table[team_name] = item  
    #pprint(league_table)
    return league_table
        
async def show_raw_standings():
    league_details = await get_league_details(league_id)
    standings = league_details["standings"]
    pprint(standings)
    
    
#asyncio.run(show_raw_standings())
#print(get_gw_info())

    
    
    