import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Connor", 20, 22, 5)
        self.drink = Drink('Tennents', 3.50, 5)

    def test_buy_drink(self):
        expected = 16.50
        self.customer.buy_drink(3.50)
        actual = self.customer.wallet
        self.assertEqual(expected,actual)

    def test_age_check(self):
        self.assertEqual(22, self.customer.age)

    # def test_increase_drunkenness(self):
    #     self.drink.alcohol_level
    #     self.assertEqual(5, self.customer.increase_drunkeness)

    def test_increase_drunkenness(self):
        expected = 5
        self.drink.alcohol_level
        actual = self.customer.drunkenness
        self.assertEqual(expected,actual)
        