"""Simple test cases to test fucntionallity """

from app import calc
from django.test import SimpleTestCase


class TestCase1(SimpleTestCase):
    """testCase 1 """

    def test_sum(self):
        """ Test adding two numbers"""

        res = calc.add(4, 6)

        self.assertEqual(res, 10)
