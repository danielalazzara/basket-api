from basket import parse_data
import pytest


@pytest.mark.parametrize("test_input,expected", [("aB c", "ab_c"), ("ABCD", "abcd"), ("abªc", "abc")])
def test_clean_up(test_input,expected):
    result = parse_data.clean_up(test_input)
    assert result == expected
