from basket import basket_app
import pytest


test_input_1 = ("catania", "messina", 45, 40)
test_expected_1 = ("catania", 2, "messina", 1)
test_input_2 = ("catania", "messina", 15, 40)
test_expected_2 = ("messina", 1, "catania", 2)

@pytest.mark.parametrize("test_input,expected", [(test_input_1, test_expected_1), (test_input_2, test_expected_2)])
def test_tournament_points(test_input,expected):
    team_1, team_2, t_1_score, t_2_score = test_input
    result = basket_app.tournament_points(team_1, team_2, t_1_score, t_2_score)
    assert result == expected

def tournament_points(team_1, team_2, t_1_score, t_2_score):
    """
    Evaluate a match and return the winning team and their points.
    :param team_1: string
    :param team_2: string
    :param t_1_score: int
    :param t_2_score: int
    :return: tuple
    """