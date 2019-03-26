import random
from card import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        self.deck = []
        for suit in suits:
            self.create_all_ranks(suit)

    def create_all_ranks(self, suit):
        for rank in ranks:
            self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
