from typing import Union
from fastapi import FastAPI, HTTPException
import basket.basket_app
import basket.parse_data


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

ALL_RESULTS = {}


@app.get("/")
def read_root():
    return {"Version": "0.1"}


@app.get("/team/{team_name}")
def return_team(team_name: str):
    if partial := [t for t in TEAMS if team_name.lower() in t.lower()]:
        _result = ALL_RESULTS or return_all_data()
        _team_data = _result.get("final_results")
        return {"result": [{"team": t, "stats_data": _team_data.get(t)} for t in partial]}
    else:
        raise HTTPException(status_code=404, detail=f'Team {team_name} not found.')


@app.get("/final_four")
def return_final_four_teams():
    _result = ALL_RESULTS or return_all_data()
    _team_data = _result.get("final_four")
    return True

@app.get("/teams")
def return_all_teams():
    all_teams = ', '.join(TEAMS)
    return all_teams


@app.get("/private/refresh_data")
def refresh_data():
    global ALL_RESULTS
    basket.parse_data.main()
    ALL_RESULTS = basket.basket_app.main()
    return 'data loaded successfully'


@app.get("/all_data")
def return_all_data():
    if ALL_RESULTS == {}:
        refresh_data()
    return ALL_RESULTS
