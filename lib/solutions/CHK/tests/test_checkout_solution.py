
from ..checkout_solution import checkout


class TestCheckout():

    def test_return_val(self):
        """
        Test return value
        """
        assert checkout("A, A") == 100

    def test_return_val_with_diffrent_items(self):
        assert checkout("A, B, C") == 100


