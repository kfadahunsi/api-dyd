import requests, json
from pprint import pprint

#this file takes any function from apifunctions.py and outputs the json data returned from its API call to a json file soit can be typed. 

base_url = "https://draft.premierleague.com/api/"

league_id = 43953

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

def get_dynamic_info():
    """
    returns dictionary with entries 'player', 'entries', 'leagues', 'time', 'active'. 
    all entries empty. might be usefull in future? maybe it requires log in. 
    """
    response = requests.get(base_url + f"bootstrap-dynamic") # nothing useful. just provides datetime
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"an error occurred {response.status_code}")
        print(response.text)
        exit(0)

data = get_dynamic_info()

with open("dynamicinfo.json", "w") as f:
    json.dump(data, f, indent=2)