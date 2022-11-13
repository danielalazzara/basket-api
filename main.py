from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
import basket.basket_app
import basket.parse_data
import visualization.build_graphs
# from fastapi.responses import FileResponse


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


@app.get("/api/team/{team_name}")
def return_team(team_name: str):
    """Search for a full team name or part of it, return simple stats"""
    if partial := [t for t in TEAMS if team_name.lower() in t.lower()]:
        _result = ALL_RESULTS or return_all_data()
        _team_data = _result.get("final_results")
        return {"result": [{"team": t, "stats_data": _team_data.get(t)} for t in partial]}
    else:
        raise HTTPException(status_code=404, detail=f'Team {team_name} not found.')


@app.get("/api/final_four")
def return_final_four_teams():
    """Simple stat results of the final four teams"""
    _result = ALL_RESULTS or return_all_data()
    _final_four_teams = _result.get('final_four').keys()
    _team_data = _result.get("final_four")
    return {"result": [{"team": t, "stats_data": _team_data.get(t)} for t in _final_four_teams]}


@app.get("/api/teams")
def return_all_teams():
    """Get all teams names from the TEAM variable"""
    all_teams = ', '.join(TEAMS)
    return all_teams


@app.get("/api/all_data")
def return_all_data():
    """Return all data"""
    if ALL_RESULTS == {}:
        refresh_data()
    return ALL_RESULTS


@app.get("/private/refresh_data")
def refresh_data():
    """Refresh the data"""
    global ALL_RESULTS
    basket.parse_data.main()
    ALL_RESULTS = basket.basket_app.main()
    return 'data loaded successfully'


@app.get("/graph")
def return_graph_main_page():
    """Return graphs"""
    return FileResponse('html/graph.html')


@app.get("/graph/all_data")
def return_graph_all_data():
    """Return graphs"""
    if ALL_RESULTS == {}:
        refresh_data()
    file_name = visualization.build_graphs.visualize_all_data(ALL_RESULTS)
    # return FileResponse(file_name)
    return file_name
