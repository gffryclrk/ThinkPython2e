import unittest

from ch18.card import Card

class TestCardClass(unittest.TestCase):

    def test_card_init(self):

        queen_of_diamonds = Card(1, 12)
        
        self.assertEqual(queen_of_diamonds.__str__(),
                         'Queen of Diamonds')

    def test_card_lt(self):

        c1 = Card(1, 1)
        c2 = Card(2, 2)

        self.assertLess(c1, c2)

        
