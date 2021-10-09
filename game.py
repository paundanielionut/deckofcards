import random

from exceptions import EmptyDeckOfCards

SUITS = ['Spade', 'Club', 'Diamond', 'Heart']
VALUES = range(1, 14)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self._build()

    def _build(self):
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))

    def order(self):
        return self.cards.sort(key=lambda c: c.value)

    def __str__(self):
        for card in self.cards:
            print(card)
        return 'end\n'

    def __len__(self):
        return len(self.cards)


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck.cards)

    def order(self):
        self.deck.cards.order(key=lambda card: card.value)

    def draw_card(self):
        if not len(self.deck):
            raise EmptyDeckOfCards("The deck is empty.")
        return self.deck.cards.pop(-1)


