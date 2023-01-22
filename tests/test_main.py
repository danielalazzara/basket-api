import pytest
from fastapi.testclient import TestClient
import main


client = TestClient(main.app)

test_input_1 = "UAA%20Aroso"
test_expected_1 = [{"team":"UAA Aroso","stats_data":{"total_points":486,"mean_points":32.4,"maximum_point":52,"minimum_point":18,"games_played":15,"wins":3,"wins_percentage":0.2}}]
test_input_2 = "Maia%20Basket"
test_expected_2 = [{"team":"Maia Basket","stats_data":{"total_points":1142,"mean_points":63.44444444444444,"maximum_point":99,"minimum_point":30,"games_played":18,"wins":17,"wins_percentage":0.9444444444444444}},{"team":"Maia Basket B","stats_data":{"total_points":498,"mean_points":38.30769230769231,"maximum_point":68,"minimum_point":16,"games_played":13,"wins":4,"wins_percentage":0.3076923076923077}}]

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Version": "0.1"}


def test_return_team_not_exist():
    response = client.get("/api/team/abcd")
    assert response.status_code == 404
    assert response.json() == {"detail":"Team abcd not found."}


@pytest.mark.parametrize("test_input, expected", [(test_input_1, test_expected_1), (test_input_2, test_expected_2)])
def test_return_team_exist(test_input, expected):
    response = client.get(f"/api/team/{test_input}")
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_return_final_four_teams():
    response = client.get("/api/final_four")
    assert response.status_code == 200
    response_body = response.json()["result"]
    assert len(response_body) == 4
    assert response_body[0]["team"] == 'FC Gaia'
    assert response_body[1]["team"] == 'FC Porto'
    assert response_body[2]["team"] == 'Maia Basket'
    assert response_body[3]["team"] == 'Club 5Basket'
