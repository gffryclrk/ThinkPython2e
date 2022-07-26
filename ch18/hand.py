"""Example code from ThinkPython 2nd Ed"""

from ch18.deck import Deck

class Hand(Deck):
    """Represents a hand of playing cards"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
