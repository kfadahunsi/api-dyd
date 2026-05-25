import json 
from pathlib import Path
from apifunctions import full_team_ids


def save_json(data, file_path):
    path = Path(file_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
def load_json(file_path):
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.resolve()}")
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def get_team_id(team_name):
    for name, team_id in full_team_ids.items():
        if team_name == name:
            return team_id