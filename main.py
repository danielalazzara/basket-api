from typing import Union
from fastapi import FastAPI, HTTPException


app = FastAPI()

TEAMS = ['AC Alfenense A', 'AC Alfenense B', 'Académico FC A',
         'Académico FC B', 'BC Gaia', 'CAA Salesianos',
         'CBP 2012 A', 'CBP 2012 B', 'CD José Regio', 'CD Póvoa A',
         'CDC J. Pacense', 'CLIP Teams', 'Campo e Sobrado',
         'Club 5Basket', 'Club 5Basket B', 'Club 5Basket C',
         'FC Gaia', 'FC Gaia B', 'FC Porto', 'FidesGondobasket',
         'GD Bolacesto', 'GDB Leça', 'Guifões SC', 'Guifões SC 2',
         'Juvemaia ACDC', 'Maia Basket', 'Maia Basket B',
         'NCR Valomgo', 'Powertoghether', 'UAA Aroso']


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/team/{team_name}")
def return_team(team_name: str, q: Union[str, None] = None):
    if team_name in TEAMS:
        return {"team": team_name}
    elif partial := [t for t in TEAMS if team_name.lower() in t.lower()]:
        return partial
    else:
        raise HTTPException(status_code=404, detail=f'Team {team_name} not found.')


@app.get("/teams")
def return_all_teams():
    all_teams = ', '.join(TEAMS)
    return all_teams
