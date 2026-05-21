import requests, json
from pprint import pprint
import pandas as pd
import sqlite3
import json
from pathlib import Path


base_url = "https://draft.premierleague.com/api/"
league_id = 43953
woga_id = 70878
entry_ids = {
        "ASA" : 224216,
        "SSFC" : 228809,
        "MMUFC" : 257018,
        "SLS" : 227314,
        "DDGP" : 237637,
        "DTF" : 312224,
    }

team_ids = {
        "ASA" : 222315,
        "SSFC" : 226964,
        "MMUFC" : 255709,
        "SLS" : 225455,
        "DDGP" : 235896,
        "DTF" : 311434,
}




headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://draft.premierleague.com/",
    "Origin": "https://draft.premierleague.com/",
    "X-API-Authorization":f"Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImRlZmF1bHQifQ.eyJjbGllbnRfaWQiOiJkZDRkZTAzYy0wZTAxLTRmN2MtOGQzNC03YTQzMjIzZDJmN2IiLCJpc3MiOiJodHRwczovL2FjY291bnQucHJlbWllcmxlYWd1ZS5jb20vYXMiLCJqdGkiOiJkMmMxNjZmZi1lYzRjLTRmNGItYmNkMS03NWM4Y2RkNTU3M2MiLCJpYXQiOjE3NzM3NDcwODAsImV4cCI6MTc3Mzc3NTg4MCwiYXVkIjpbImh0dHBzOi8vYXBpLnBpbmdvbmUuZXUiXSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInN1YiI6Ijc4NmI0MDc0LWE3ZDYtNGJhOC1iYTA5LWVmMTI5NjY0OWEyNSIsInNpZCI6IjlhYjNmNDc3LTkzNTItNDkyNy04OWQzLTkzNTM2Mzk1NTY3MiIsImF1dGhfdGltZSI6MTc3Mzc0NzA3OCwiYWNyIjoiMjYyY2U0YjAxZDE5ZGQ5ZDM4NWQyNmJkZGI0Mjk3YjYiLCJhdXRoZW50aWNhdG9yIjoicHdkIiwiaHR0cDovL21lZGlha2luZC5jb20vbWYvdGlkIjoiZGVmYXVsdCIsImVudiI6IjY4MzQwZGUxLWRmYjktNDEyZS05MzdjLTIwMTcyOTg2ZDEyOSIsIm9yZyI6IjNhNjg1MDMyLTgzMjYtNDk2OS1hNzhiLWNjMjk3NzViMTNkNiIsInAxLnJpZCI6IjJmY2ExOWFhLTQyZWEtNDc3NS05NzliLWM5MDc2ODJlYTgyMCJ9.OVk96Gi1C8lObywscspBl0q4gsL0Rm6E6AUcw_TwerjkgA6K6ImDvIOviYSosEh1fwBW0wiw9k9LN1swmiaACWwYaAp5LOerCWcf8zLSESdbtytF9c3TcDZy-u2i2cyukoWwu6e1Pm0FCMDRjbiCSdxQhjF4tRRuwzrl0vrkoDHVz4n7n7FALWx5IwoKyhxer_JwjahOFruiSUY0MF5bp3_BDtojZ12SHv4BnoTRw6LeGxGeG8rNxBMKtNTFroDiBV7CZOqK__p-LdSk1cA5Yr5VA0xpI07lz1b7mFp_I_lb3wBemk0Yzu3xXhXT7ySVtgbK_X42Pm_HAPgn1FDXwg"
}

# login
#r = session.post(login_url, data=payload, headers=headers)
#print(r.status_code)


def create_league_dict(base_url, league_id):
    '''
    make an API reuest and receive JSON file for specified league in FPL draft
    Parameters:
    base_url (string): is the url for the FPL draft API
    league_id (list): is the id number gotten from FPL draft website
    returns:
    league_dict (dictionary): dictionary of key league information
    '''
    response = requests.get(base_url + f"league/{league_id}/details")
    
    if response.status_code == 200:
        league_dict = response.json()
        return league_dict
    else:
        print(f"an error occurred {response.status_code}")
        exit(0)
    
    #pprint(league_obj, indent=2, depth=1, compact=True)

def get_ids(league_dict):
    '''
    retrieve league entry ids from the league dictionary and return them in a list
    Parameters:
    league_dict (dictionary): the dictionary containing the league information
    returns:
    league_ids (list): list of each league members FPL id
    '''

    team_ids = []
    
    for element in league_dict["league_entries"]:
        id = element["entry_id"]
        team_ids.append(id)
    
    return team_ids

def get_team_names(league_dict):
    '''
    retrieve team names from the league dictionary and return them in a list
    Parameters:
    league_dict (dictionary): the dictionary containing the league information
    returns:
    league_ids (list): list of each league members FPL id
    '''

    team_names = []
    
    for element in league_dict["league_entries"]:
        name = element["entry_name"]
        team_names.append(name)
    
    return team_names


def create_teams_dict(base_url, team_ids):
    '''
    make an API reuest and receive JSON file of teams in league in order to make a dictionary of them
    Parameters:
    base_url (string): is the url for the FPL draft API
    team_ids (list): is a list of the ids for the draft league teams gotten from FPL draft website
    returns:
    dictionary: dictionary of dictionaries containing information for each team in the team_ids list
    '''
    team_dict = {}
    for id in team_ids:
        response = requests.get(base_url + f"entry/{id}/public")
        if response.status_code == 200:
            team = response.json()
            team_dict[id] = team
        else:
            print(f"an error occurred {response.status_code}")
            exit(0)
    return team_dict

def create_team_data(team_names, team_dict):
    '''
    create a dictionary of dictionaries for each team in the league holding their data
    team_dict (dictionary): is the url for the FPL draft API
    team_names (dictionary): is a list of the ids for the draft league teams gotten from FPL draft website
    returns:
    dictionary: dictionary of dictionaries for each team in the league holding their data
    '''

    individual_data = {}
    team_data = {}

    for id in team_dict:

        #print("this is the current team  " + team_dict[id]["entry"]["name"])
        #print("this is theier current score  " + str(team_dict[id]["entry"]["event_points"]))
        individual_data["gw score"] = team_dict[id]["entry"]["event_points"]
        individual_data["total score"] = team_dict[id]["entry"]["overall_points"]
        team_data[team_dict[id]["entry"]["name"]] = individual_data


    #print(team_data)

def gw_num(base_url):
    '''
    make an API reuest and receive JSON file with information about the current gw
    Parameters:
    base_url (string): is the url for the FPL draft API
    league_id (list): is a list of the ids for the draft league teams gotten from FPL draft website
    returns:
    dictionary: the current gw number
    '''
    response = requests.get(base_url + f"game") 
    
    if response.status_code == 200:
        gw_info = response.json()
        gw_num = gw_info["current_event"]
    else:
        print(f"an error occurred {response.status_code}")
        exit(0)
    return gw_num

def get_current_gw(base_url, id, gw):
    '''
    make an API reuest and receive JSON file of teams in league and all their information for that GW. Will form the basis for calculating POB
    Parameters:
    base_url (string): is the url for the FPL draft API
    team_ids (list): is a list of the ids for the draft league teams gotten from FPL draft website
    gw (int): is the gameweek number
    returns:
    dictionary: dictionary of dictionaries for each team in the team_ids list
    '''

    response = requests.get(base_url+ f"entry/{id}/event/{gw}")
    if response.status_code == 200:
        requested_gw = response.json()
    else:
        print(f"an error occurred {response.status_code}")
        exit(0)

    return  requested_gw

def get_all_gws(base_url, team_ids):
    test_ids = team_ids[:2]
    teams_gws = {}
    gw_list = []
    for id in test_ids:
        for gw in range(1, gw_num(base_url)+1):
           current_gw = get_current_gw(base_url, id, gw)
           gw_list.append(current_gw)
        teams_gws[id] = gw_list.copy()
        gw_list.clear()
    pprint(teams_gws)
    #return teams_gws
    


def call_api_tester(base_url, entry_id, team_id, league_id):

    #response = requests.get(base_url + f"bootstrap-dynamic") # nothing useful. just provides datetime
    #response = requests.get(base_url + f"game") #provides info on current and next gw and whether waivers have been processed
    #response = requests.get(base_url + f"bootstrap-static") #massive data dump of all players, teams, positions, etc
    #response = requests.get(base_url + f"league/{league_id}/details") #league creation info, league entrants info and current standings
    #response = requests.get(base_url + f"league/{league_id}/element-status") # true or false on whether a player has been in an accepted trade
    #response = requests.get(base_url + f"draft/league/{league_id}/trades") #all trades made in the league
    #response = requests.get(base_url + f"draft/entry/{team_id}/transactions", headers=headers) #unable to check because of team ID
    #response = requests.get(base_url + f"pl/event-status") #confirms that bonus points have been added with each day in the gw
    #response = requests.get(base_url + f"event/{30}/live") #every player in the game and their stats for current gw
    #response = requests.get(base_url + f"entry/{team_id}/my-team") #unable to check because of team ID
    response = requests.get(base_url + f"entry/{entry_id}/public") #shows team information eg gw points, player name, total transactions etc
    #response = requests.get(base_url + f"draft/{league_id}/choices") #unclear what the information is
    #response = requests.get(base_url + f"watchlist/{team_id}" , headers=headers) #unable to check because of team ID
    #response = requests.get(base_url + f"entry/{entry_id}/event/{30}") #shows 15 man squad and their info

    if response.status_code == 200:
        test_dict = response.json()
        pprint(test_dict)
        #'elements', 'element_types', 'element_stats', 'events', 'fixtures', 'settings', 'teams'
    else:
        print(f"an error occurred {response.status_code}")
        print(response.text)
        exit(0)



def testing():

    #link1 = f"https://draft.premierleague.com/api/entry/{woga_entry_id}/my-team"
    #link2 = f"https://draft.premierleague.com/api/watchlist/{woga_entry_id}"
    #link3 = f"https://draft.premierleague.com/api/entry/{woga_entry_id}/event/{33}"
    link4 = f"https://draft.premierleague.com/api/draft/entry/{woga_entry_id}/transactions"
    response = requests.get(link4)
    if response.status_code == 200:
        test_dict = response.json()
        pprint(test_dict)
    else:
        print(f"an error occurred {response.status_code}")
        exit(0)    


#league_dict = create_league_dict(base_url, league_id)
#team_ids = get_ids(league_dict)
#team_names = get_team_names(league_dict)
#team_dict = create_teams_dict(base_url, team_ids)

call_api_tester(base_url, entry_ids["ASA"], team_ids["ASA"], league_id)
#current_gw = get_current_gw(base_url, team_ids, 25)
#create_team_data(team_names, team_dict)
#get_all_gws(base_url, team_ids)
#testing()


#pprint(num)
#pprint(team_dict, indent=2, depth=5, compact=True)

#league_setup = league_dict["league"]
#league_teams = league_dict["league_entries"]
#league_standings = league_dict["standings"]

#pprint(league, indent=2, depth=1, compact=True)
#pprint(league_entries, indent=2, depth=1, compact=True)
#pprint(standings, indent=2, depth=1, compact=True)