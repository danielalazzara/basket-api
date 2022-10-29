# basket-api
This application, based on FastAPI, presents the data generated with `basket`.

```
curl http://127.0.0.1:8000/final_four | jq

{
  "result": [
    {
      "team": "FC Gaia",
      "stats_data": {
        "total_points": 1062,
        ....
```

## requirements
- python >= 3.10
- `pip install -r requirements.txt`

## usage
Start Uvicorn in the terminal:
```
(basket-api-venv) ➜  basket-api git:(main) ✗ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/danielalazzara/github/basket-api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
Access the app locally on `127.0.0.1:8000`:
```
curl  http://127.0.0.1:8000/
```

### Search a team
You can search a team with is full name. For Example:
```
curl http://127.0.0.1:8000/team/FC%20Gaia%20B
```
with the following result:
```
{"result":[{"team":"FC Gaia B","stats_data":{"total_points":313,"mean_points":31.3,"maximum_point":50,"minimum_point":4,"games_played":10,"wins":4,"wins_percentage":0.4}}]}%
```

Or you can search by providing part of the name:
```
curl http://127.0.0.1:8000/team/gaia
```
with the following result:
```
{"result":[{"team":"BC Gaia","stats_data":{"total_points":330,"mean_points":41.25,"maximum_point":62,"minimum_point":0,"games_played":8,"wins":6,"wins_percentage":0.75}},{"team":"FC Gaia","stats_data":{"total_points":1062,"mean_points":59.0,"maximum_point":140,"minimum_point":36,"games_played":18,"wins":11,"wins_percentage":0.6111111111111112}},{"team":"FC Gaia B","stats_data":{"total_points":313,"mean_points":31.3,"maximum_point":50,"minimum_point":4,"games_played":10,"wins":4,"wins_percentage":0.4}}]}%
```


### Get the data of the final four teams
```
curl http://127.0.0.1:8000/final_four
```

## Reference
This application uses FastAPI: https://fastapi.tiangolo.com