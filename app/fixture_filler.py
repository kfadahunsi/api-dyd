from helper_functions import load_json, save_json
from pathlib import Path
from pprint import pprint
from apifunctions import full_team_ids
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def get_team_id(team_name):
    for name, team_id in full_team_ids.items():
        if team_name == name:
            return team_id
    

def fill_cup_table():
    fixture_path = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "cup_fixtures", "25_26.json"))
    history_path = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "table_history", "25_26.json"))
    
    fixtures = load_json(fixture_path)
    gw_history = load_json(history_path)

    if gw_history and fixtures:
        for gw, standings in gw_history.items():
            for fixture in fixtures:
                if int(gw.split(" ")[1]) == fixture["week"]:
                    for standing in standings:
                        if get_team_id(fixture["home"]) == standing["league_entry"]:
                            fixture["home_score"] = standing["event_total"]
                        elif get_team_id(fixture["away"]) == standing["league_entry"]:
                            fixture["away_score"] = standing["event_total"]
                            
        save_json(fixtures, fixture_path)
    else:
        print("please ensure that the fixture and gw history files exist.")
                    
                
    
    #pprint(fixtures)
    
fill_cup_table()
#print(full_team_ids)