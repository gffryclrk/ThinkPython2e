import unittest

from ch18.card import Card
from ch18.hand import Hand
from ch18.deck import Deck

class TestCardClass(unittest.TestCase):

    def test_card_init(self):

        queen_of_diamonds = Card(1, 12)
        
        self.assertEqual(queen_of_diamonds.__str__(),
                         'Queen of Diamonds')

    def test_card_lt(self):

        c1 = Card(1, 1)
        c2 = Card(2, 2)

        self.assertLess(c1, c2)

    def test_hand(self):
        """ Given a Hand the Deck should be able to move cards without throwing an exception """
        h = Hand()
        d = Deck()

        d.move_cards(h, 10)


        

        
