from pprint import pprint
from apifunctions import get_gw_info, make_league_table
import asyncio
from helper_functions import load_json, save_json
from pathlib import Path
from config import league_id
import os




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fixture_path = os.path.join(BASE_DIR, "..", "data", "cup fixtures", "25_26.json")
fixtures = load_json(fixture_path)
print(fixtures)

def print_table(table):
    for team, stats in table.items():
        print(team + " P: " + str(stats["played"]) +" W: "+ str(stats["wins"]) +" L: " + str(stats["losses"]) +" PF: " + str(stats["points_for"]) +" PA: " + str(stats["points_against"]) +" PTS: " + str(stats["league_points"]))

def get_initial_team_stats():
    return {
        "Amassing Silvaware": {"played": 0,"wins": 0,"draws": 0, "losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
        "Duck Duck Guus Poyet": {"played": 0,"wins": 0,"draws": 0,"losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
        "Darwin’s Theory": {"played": 0,"wins": 0,"draws": 0,"losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
        "Maatsen Margiela Utd": {"played": 0,"wins": 0,"draws": 0,"losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
        "Saint Laurent Slot": {"played": 0,"wins": 0,"draws": 0,"losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
        "Super Slimey Fütbol": {"played": 0,"wins": 0,"draws": 0,"losses": 0,"points_for": 0,"points_against": 0,"league_points": 0,},
    }       
        
def process_match(team_stats, home_team, away_team, home_score, away_score):
    """
    checks the home score and away score for each fixture. updates the team stats table.
    
    win - awards 3 points for a win, updates win count for that team and loss count for the other team. 
    updates fplpoints for and against for both, updates played count for both sides
    
    loss - awards 0 points for a loss, updates loss count for that team and win count for the other team. 
    updates fplpoints for and against for both, updates played count for both sides
    
    draw - awards 1 point for each side, updates draw count for both sides. 
    updates fplpoints for and against for both, updates played count for both sides
    """
    #update games played
    team_stats[home_team]["played"] +=1
    team_stats[away_team]["played"] +=1
    
    #update points for and against
    team_stats[home_team]["points_for"] += home_score
    team_stats[home_team]["points_against"] += away_score
    team_stats[away_team]["points_for"] += away_score
    team_stats[away_team]["points_against"] += home_score
    
    #results logic
    if home_score > away_score:
        team_stats[home_team]["wins"] += 1
        team_stats[home_team]["league_points"] += 3
        team_stats[away_team]["losses"] += 1

        
    
    elif away_score > home_score:
        team_stats[away_team]["wins"] += 1
        team_stats[away_team]["league_points"] += 3        
        team_stats[home_team]["losses"] += 1

    
    else: 
        team_stats[home_team]["draws"] +=1 
        team_stats[away_team]["draws"] +=1 
        
        team_stats[home_team]["league_points"] +=1
        team_stats[away_team]["league_points"] +=1
        

        
         
def process_fixtures(team_stats, fixtures):
    """
    loops through each fixture in the table and confirms if it is in the week range to be processed. 
    if yes, calls the process match function for the fixture
    """
    
    for fixture in fixtures:
        #skip unplayed fixtures
        if fixture["home_score"] is None:
            continue
        process_match(team_stats, fixture["home"], fixture["away"], fixture["home_score"], fixture["away_score"])
            
            
def produce_league_table():
    team_stats = get_initial_team_stats()
    process_fixtures(team_stats, fixtures)
    return dict(sorted(team_stats.items(), key= lambda item:( 
        item[1]["league_points"],
        item[1]["points_for"],
        ), reverse=True))


async def get_semis():
    cup_table = {}
    semi_finals = {}
    gw_info = await get_gw_info()
    if gw_info["current_event"] == 36 and gw_info["current_event_finished"] == True: #remember to change the first condition to 36 and  the second condition to True 
        cup_table = produce_league_table()
        semi_finalists = list(cup_table.keys())[0:4]
        semi_finals["1"] = {"home":semi_finalists[0], "away":semi_finalists[3], "home_score": None, "away_score": None}
        semi_finals["2"] = {"home":semi_finalists[1], "away":semi_finalists[2], "home_score": None, "away_score": None}

        return semi_finals
    elif gw_info["current_event"] > 36:
        cup_table = produce_league_table()
        semi_finalists = list(cup_table.keys())[0:4]
        semi_finals["1"] = {"home":semi_finalists[0], "away":semi_finalists[3], "home_score": None, "away_score": None}
        semi_finals["2"] = {"home":semi_finalists[1], "away":semi_finalists[2], "home_score": None, "away_score": None}

        return semi_finals
    else: 
       return None
       
async def get_semi_results():
    semi_finalists = {}
    league_table = {}
    gw_info = await get_gw_info()
    if gw_info["current_event"] == 37 and gw_info["current_event_finished"] == True: #remember to change the first condition to 36 and  the second condition to True  
        semi_finalists = await get_semis()
        league_table = await make_league_table()
        for semifinal in semi_finalists.values():
           for team_name, team_info in league_table.items():
               if team_name == semifinal["home"]:
                   semifinal["home_score"] = team_info["event_total"]
               if team_name == semifinal["away"]:
                   semifinal["away_score"] = team_info["event_total"]
                   
        return semi_finalists
                   
    elif gw_info["current_event"] == 37 and gw_info["current_event_finished"] == True: #remember to change the first condition to 36 and  the second condition to True  
        semi_finalists = await get_semis()
        league_table = await make_league_table()
        for semifinal in semi_finalists.values():
           for team_name, team_info in league_table.items():
               if team_name == semifinal["home"]:
                   semifinal["home_score"] = team_info["event_total"]
               if team_name == semifinal["away"]:
                   semifinal["away_score"] = team_info["event_total"]
                   
                   
        save_json(semi_finalists, "gw37table.json")
        return semi_finalists
    
    elif gw_info["current_event"] > 37:
        semi_finalists = load_json("gw37table.json")

        return semi_finalists
    
    else:
        return None

async def get_finalists():
    finalists = {}
    gw_info = await get_gw_info()
    
    if gw_info["current_event"] == 37 and gw_info["current_event_finished"] == True: 
        semi_results = await get_semi_results()
        if semi_results["1"]["home_score"] > semi_results["1"]["away_score"]:
            finalists["home"] = {"name": semi_results["1"]["home"], "score": None}
            
        elif semi_results["1"]["away_score"] > semi_results["1"]["home_score"]:
            finalists["home"] = {"name" : semi_results["1"]["away"], "score": None}
            
        if semi_results["2"]["home_score"] > semi_results["2"]["away_score"]:
            finalists["away"] = {"name" : semi_results["2"]["home"], "score" : None}
        
        if semi_results["2"]["away_score"] > semi_results["2"]["home_score"]:
            finalists["away"] = {"name" : semi_results["2"]["away"], "score" : None}
        
        return finalists
    else:
        return None

#need to add a true or false property to denote when the gw is over otherwise the frontend will display a winner before time is right    
async def get_finals():
    finals = await get_finalists()
    gw_info = await get_gw_info()
    
    if gw_info["current_event"] == 37 and gw_info["current_event_finished"] == True:
        return finals
    
    
    elif gw_info["current_event"] == 38 and gw_info["current_event_finished"] == False:
        league_table = await make_league_table()
        for finalist in finals.values():
            for club, info in league_table.items():
                if finalist["name"] == club:
                    finalist["score"] = info["event_total"]
        return finals
    
    
    elif gw_info["current_event"] == 38 and gw_info["current_event_finished"] == True:
        league_table = await make_league_table()
        for finalist in finals.values():
            for club, info in league_table.items():
                if finalist["name"] == club:
                    finalist["score"] = info["event_total"]
        #save_json(finals, "finals.json")
        return finals
    else:
        return None

async def get_winner():
    league_table = {}
    finals = {}
    winner = {}
    gw_info = await get_gw_info()
    if gw_info["current_event"] == 38 and gw_info["current_event_finished"] == False: #remember to change the first condition to 36 and  the second condition to True
        finals =  await get_finals()
        league_table = await make_league_table()
        for team, details in league_table.items():
            for club in finals.values():
                if team == club["name"]:
                    club["score"] = details["event_total"]
        winner = max(finals.values(), key= lambda team: team["score"])
        return winner
    else:
        return None

         
#print_table(produce_league_table())

"""
pprint(cup_table, sort_dicts=False) if we neeed to print an ordered dict using pprint we have to make sorting False 
"""
    
#asyncio.run(get_winner())   




    
