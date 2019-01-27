import unittest
from array_addition import array_addition


class TestArrayAddition(unittest.TestCase):

    def setUp(self):
        self.big_list = [1, 2, 3, 4, 5, 6, 7]
        self.first_half = [1, 2, 3]
        self.second_half = [4, 5, 6, 7]
        self.answer = [28]
        self.iterations = 3

    def test_split_list(self):
        a, b = array_addition.split_list(self.big_list)
        self.assertEqual(self.first_half, a)
        self.assertEqual(self.second_half, b)





