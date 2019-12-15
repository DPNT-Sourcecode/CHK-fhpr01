
from .. checkout_solution import checkout


def test_checkout():
    """
    Test return value
    """
    assert checkout("A, A") == 30

