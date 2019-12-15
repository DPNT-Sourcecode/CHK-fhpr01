from .sum_solution import get_total_value


def test_get_total_value():
    x = 15
    y = 5
    assert get_total_value(x, y) == 20
