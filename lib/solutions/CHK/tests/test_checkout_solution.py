
from ..checkout_solution import checkout


class TestCheckout():

    def test_illegal_val(self):
        assert checkout(256) == -1

    def test_return_val(self):
        """
        Test return value
        """
        assert checkout("A, A") == 100

    def test_return_val_with_diffrent_items(self):
        assert checkout("A, B, C") == 100

    def test_multi_items_of_the_same_type(self):
        assert checkout("A, B, A") == 130

    def test_multi_itmes_offer(self):
        assert checkout("A, A, B, A") == 160

    def test_multiple_multi_itmes_offers(self):

        assert checkout("A, A, B, A, A, A, A") == 160


