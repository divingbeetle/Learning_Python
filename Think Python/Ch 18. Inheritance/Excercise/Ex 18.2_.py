"""

*** EX 18.2 ***
    Write a Deck method called deal_hands that takes two parameters,
    the num of hands and num of cards per hand.

    It should created the appropriate number of Hand objects,
    deal the appropriate number of cards per hand,
    and return a list of Hands.

"""
import random


class Card:
    """Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        deal_hands = []
        d = {}
        for i in range(1, num_hands + 1):
            d["player" + str(i)] = None
        for player_name in d:
            deal_hands.append(Hand(player_name))

        for player in deal_hands:
                self.move_cards(player, num_cards)
        return deal_hands



class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, lable=''):
        self.cards = []
        self.lable = lable


deck = Deck()
deck.shuffle()
player_hands = deck.deal_hands(3, 5)
print(player_hands)
for player_hand in player_hands:
    print(player_hand.lable)
    print(player_hand)