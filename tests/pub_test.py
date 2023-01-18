import unittest

from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Angels", 500, "Tennents")
        self.customer = Customer("Taylor", 20, 25, 12)

    def test_increase_till(self):
        expected = 503.50
        self.pub.increase_till(3.50)
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_refuse_service(self):
        expected = self.customer.drunkenness
        self.pub.refuse_service(4)
        actual = self.customer.drunkenness
        self.assertEqual(expected,actual)

   
