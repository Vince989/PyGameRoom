# -*- coding: utf-8 -*-
from .PlayingCardPile import PlayingCardPile
from .PlayingCard import RANK_A


class Blackjack(object):
    def __init__(self, players=1):
        """
        A game of Blackjack, with a Dealer playing with N players

        :param int players: Number of players
        """
        super().__init__()

        self.debug = True

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

        if self.debug:
            print("Dealer's initial hand : {}".format(self.dealer))
            for hand in self.hands:
                print("Player's initial hand : {}".format(hand))

    def play_console(self):
        if self.debug:
            for hand in self.hands:
                print(self.eval_blackjack_score(hand.items))

    @staticmethod
    def eval_blackjack_score(hand):
        score = 0
        aces = 0
        faces = 0

        # Remember it if there's at least an Ace, and "ceil off" the Faces
        for card in hand:
            if card.rank == RANK_A:
                aces += 1
            if card.rank > 10:
                card.rank = 10
                faces += 1
            score += card.rank

        if len(hand) == 2 and aces and faces:  # Blackjack!
            score = 21
        elif aces and score < 11:  # Add the Ace value if there's room
            score += 10

        return score

    # To complete...
