# -*- coding: utf-8 -*-
from .PlayingCardPile import PlayingCardPile


class Blackjack(object):
    def __init__(self, players=1):
        """
        A game of Blackjack, with a Dealer playing with N players

        :param int players: Number of players
        """
        super().__init__()

        self.hands = {}  # The various players' hands

        self.deck = PlayingCardPile(full_decks=6)
        self.deck.shuffle()

        # Draw 1 card for each player, then the dealer,
        # then another one for each player
        for number in range(players):
            self.hands[number] = PlayingCardPile()
            self.hands[number] = self.deck.take(1)
        self.dealer = self.deck.take(1)
        for player in range(players):
            self.hands[player] = self.deck.take(1)

    def play(self):
        for hand in self.hands.items():
            print("Player {}'s initial hand : {}".format(hand[0], hand[1]))

    # TODO To complete...
