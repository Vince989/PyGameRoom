# -*- coding: utf-8 -*-
from .PlayingCardPile import PlayingCardPile


class Blackjack(object):
    def __init__(self, players=1):
        """
        A game of Blackjack, with a Dealer playing with N players

        :param int players: Number of players
        """
        super().__init__()

        self.hands = []  # The players' hands

        self.deck = PlayingCardPile(full_decks=6)
        self.deck.shuffle()

        # Init and draw 1 card for each player, then one for the dealer,
        # then another one for each player
        for player in range(players):
            self.hands.append(PlayingCardPile())
            self.hands[player].add(self.deck.take(1))

        self.dealer = PlayingCardPile()
        self.dealer.add(self.deck.take(1))

        for player in range(players):
            self.hands[player].add(self.deck.take(1))

        # Debug info
        if True:
            print("Dealer's hand : {}".format(self.dealer))
            for hand in self.hands:
                print("Player's initial hand : {}".format(hand))

    def play_console(self):
        for hand in self.hands:
            print(self.eval_score(hand.items))
            pass

    def eval_score(self, hand):
        score = 0
        for card in hand:
            pass
        return score

    # To complete...
