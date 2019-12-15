
from ..checkout_solution import checkout


class TestCheckout():

    def test_return_val(self):
        """
        Test return value
        """
        assert checkout("A, A") == 100


