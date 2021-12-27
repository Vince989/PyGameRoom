# -*- coding: utf-8 -*-
from .PlayingCardPile import PlayingCardPile


class Poker(object):
    def __init__(self, players=1):
        """
        The classic version of Poker, with 5 cards dealt at the start

        :param int players: Number of players
        """
        super().__init__()

        self.hands = {}  # The various players' hands

        self.deck = PlayingCardPile(full_decks=1)
        self.deck.shuffle()

        for player in range(players):
            self.hands[player] = self.deck.deal(5)

    def play(self):
        for hand in self.hands.items():
            print("Player {}'s hand : {}".format(hand[0], hand[1]))

    # TODO To complete...
