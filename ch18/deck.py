"""Example code from ThinkPython 2nd Ed"""

from card import Card

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        return '\n'.join([str(c) for c in self.cards if c])

if __name__ == '__main__':

    d = Deck()
    print(d)

