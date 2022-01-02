# -*- coding: utf-8 -*-
from Game import Game
from .PlayingCardPile import PlayingCardPile
from .PlayingCard import RANK_A


class Blackjack(Game):
    def __init__(self, num_players=1):
        """
        A game of Blackjack, with a Dealer playing with N players

        :param int num_players: Number of players
        """
        super().__init__(num_players)

        self.debug = True  # Show some more info

        # Supposed to be always 6 decks in Blackjack ??
        self.deck = PlayingCardPile(full_decks=6)
        self.deck.shuffle()

        self.dealer = PlayingCardPile()

        self.setup()

    def setup(self):
        # Init and draw 1 card for each player, then one for the dealer,
        # then another one for each player
        for player in self.players:
            player.hand = PlayingCardPile()
            player.hand.add(self.deck.take(1))

        self.dealer.add(self.deck.take(1))

        for player in self.players:
            player.hand.add(self.deck.take(1))

        if self.debug:
            print("Dealer's first card : {}".format(self.dealer))
            for player in self.players:
                print("Player {}'s initial hand : {}".format(player.name, str(player.hand)))

    def play_console(self):
        for player in self.players:
            choice = ""
            while choice not in ["stand"]:
                print("\nPlayer {}, your hand is : {}".format(player.name, str(player.hand)))
                choice = input("Your hand is worth {}, what do you wanna do? (hit/stand) : ".
                               format(self.eval_score(player.hand))).lower()

                if choice == "hit":
                    player.hand.add(self.deck.take(1))

        self.dealer.add(self.deck.take(1))
        print("\nDealer's initial hand : {}, worth {}".format(
            str(self.dealer), self.eval_score(self.dealer)))

        while self.eval_score(self.dealer) < 17:
            self.dealer.add(self.deck.take(1))
            print("Dealer's new hand : {}, worth {}".format(
                str(self.dealer), self.eval_score(self.dealer)))

    @staticmethod
    def eval_score(player):
        score = 0
        aces = 0
        faces = 0

        # Remember it if there's at least an Ace, and "ceil off" the Faces
        for card in player.items:
            if card.rank == RANK_A:
                aces += 1
            if card.rank > 10:
                card.rank = 10
                faces += 1
            score += card.rank

        if len(player.items) == 2 and aces and faces:  # Blackjack!
            score = 21
        elif aces and score < 11:  # Add the Ace value if there's room
            score += 10

        return score
