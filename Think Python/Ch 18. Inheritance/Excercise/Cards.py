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

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Represents a deck of cards."""

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

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for _ in range(num):
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
    def __init__(self, label=""):
        self.cards = []
        self.label = label