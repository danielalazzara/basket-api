import pytest
from fastapi.testclient import TestClient
import main


client = TestClient(main.app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Version": "0.1"}


def test_return_team_not_exist():
    response = client.get("/api/team/abcd")
    assert response.status_code == 404
    assert response.json() == {"detail":"Team abcd not found."}


def test_return_team_exist():
    response = client.get("/api/team/UAA%20Aroso")
    assert response.status_code == 200
    assert response.json() == {"result":[{"team":"UAA Aroso","stats_data":{"total_points":486,"mean_points":32.4,"maximum_point":52,"minimum_point":18,"games_played":15,"wins":3,"wins_percentage":0.2}}]}

