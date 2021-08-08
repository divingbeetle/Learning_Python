"""

*** EX 18.3 ***
    Add Methods to Pockerhand() named has_pair, has_twopair, etc
    that return True or False according to whether hte relevent criteria.
    Your code should work correctly for "hands" that contain any number of cards.

    Write a method named classify that figures out the highest-value classification
    for a hand and sets the label attribute accordingly

    When you are convinced that your classification methods are working.
    estimate the probabilities of the various hands. Write a function that
    shuffles a deck of cards, divides it into hand, and counts the num of times
    various classifications appear

    print a table of the classifications and their probabilities
    Run your program with larger and larger numbers of hands until
    the output values converge to a resonable degree of accuracy

"""

import random
from statsmodels.stats.proportion import proportions_ztest
from Cards import *


class PokerHand(Hand):
    """Represents a poker hand."""
    rank_names = ["none", "pair", "two pairs", "three of a kind", "straight",
                  "flush", "full house", "four of a kind", "straight flush"]

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hist()
        l = [value for value in self.ranks.values()]
        if 4 in l:
            self.handrank[7] = True
        elif 3 in l:
            if 2 in l:
                self.handrank[6] = True
            self.handrank[3] = True
        elif 2 in l:
            if l.count(2) >= 2:
                self.handrank[2] = True
            else:
                self.handrank[1] = True
        else:
            self.handrank[0] = True

    def has_straight(self):
        self.rank_hist()
        l = [rank for rank in self.ranks]
        l.sort()
        diff = [str(l[i + 1] - l[i]) for i in range(len(l) - 1)]
        if '1111' in "".join(diff):
            self.handrank[4] = True

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits.setdefault(card.suit, []).append(card.rank)

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if len(val) >= 5:
                val.sort()
                diff = [str(val[i + 1] - val[i]) for i in range(len(val) - 1)]
                if '1111' in "".join(diff):
                    self.handrank[8] = True
                else:
                    self.handrank[5] = True

    def classify(self):
        self.handrank = [False] * 9
        self.has_flush()
        self.has_pair()
        self.has_straight()
        reverse = self.handrank[::-1]
        i = 8 - reverse.index(True)
        self.label = PokerHand.rank_names[i]


def get_frequency(num_hands, N):
    d = {}
    for i in range(N):
        deck = Deck()
        deck.shuffle()

        hand = PokerHand()
        deck.move_cards(hand, num_hands)
        hand.classify()
        d[hand.label] = d.get(hand.label, 0) + 1
    return d


def do_proptest(freq, known, N):
    for key, value in freq.items():
        print(f"for {key}")
        print(f"P0 : {known[key] / 100}")
        print(f"P  : {freq[key] / N}\n")
        _, pvalue = proportions_ztest(count=freq[key], nobs=N, value=known[key]/100)
        if pvalue > 0.05:
            print(f"p-value: {pvalue:.5f}\nThe result follows known probability in a=0.05\n")
        else:
            print(f"p-value: {pvalue:.5f}\nThe result doesn't follow known probability in a=0.05\n")


def main():
    card7_known = {"none": 17.4119, "pair": 43.8225, "two pairs": 23.4955, "three of a kind": 4.8298,
                   "straight": 4.6193,
                   "flush": 3.0254, "full house": 2.60, "four of a kind": 0.168, "straight flush": 0.03108}
    card5_known = {"none": 50.1177, "pair": 42.2569, "two pairs": 4.7539, "three of a kind": 2.1128, "straight": 0.3925,
                   "flush": 0.1965, "full house": 0.1441, "four of a kind": 0.02401, "straight flush": 0.00139}

    freq1 = get_frequency(7, 10000)
    do_proptest(freq1, card7_known, 10000)

    freq2 = get_frequency(5, 10000)
    do_proptest(freq2, card5_known, 10000)


if __name__ == '__main__':
    main()




