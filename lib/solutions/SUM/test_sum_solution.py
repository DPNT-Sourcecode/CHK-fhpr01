from .sum_solution import get_total_value


def compute():
    """
    Total number should add up to
    20
    """
    x = 15
    y = 5
    assert get_total_value(x, y) == 20
