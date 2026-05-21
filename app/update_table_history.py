from helper_functions import load_json, save_json
from pathlib import Path
from pprint import pprint
from apifunctions import get_gw_info, make_league_table, get_league_details, league_id
import asyncio

"""
the purpose of this script is to store the weekly table updates from fpl draft api
which only provides a snapshot of each week and then is lost once the week has passed. 
with this we can preserve each week in a JSON file and load it to use for things like the draft cup etc.
"""

"""
at the start of a new season, change the file_path variable to a new name with the season year so that the information
can be generated and put into a new json file. 
"""


    
def check_gw(hist_dict, current_gw):
    for gw in hist_dict.keys():
        if gw == current_gw:
            return True
        
    return False
        
async def update_gw_history():
   
    file_path = r"C:\Users\Kevwe Fadahunsi\Documents\Coding\React Portfolio\api-dyd\data\table history\25_26.json"
    
    gw_info = await get_gw_info()
    details = await get_league_details(league_id)
    standings = details["standings"]

    gw = gw_info["current_event"]
    gw_key = "Gameweek " + str(gw)
    
    
    if gw_info["current_event_finished"] == False: #remember to change the bool to false false means it will not add an incomplete gw to the json
        print("gw incomplete, exiting program")
        return
    else:
        path = Path(file_path)
        if path.exists():
            print("path exists")
            gw_history = load_json(file_path)
            
            if check_gw(gw_history, gw_key) == True:
                print("Complete table, nothing added")
                return
            else:
                gw_history[gw_key] = standings 
                print(f"saving {gw_key} to {file_path}")
                save_json(gw_history, file_path) 
                #pprint(gw_history)
        else:
            print("path does not exist, will be created")
            history = {}
            history[gw_key] = standings
            print("saving new history table")
            save_json(history, file_path)
            #pprint(history)

asyncio.run(update_gw_history())