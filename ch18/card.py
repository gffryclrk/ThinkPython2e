"""Example code from ThinkPython 2nd Ed"""


class Card:
    """Represents a standard playing card"""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
        
