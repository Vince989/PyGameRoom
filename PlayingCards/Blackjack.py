# -*- coding: utf-8 -*-
from Game import Game
from Player import Player
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

        self.dealer = Player("DEALER")
        self.dealer.hand = []
        self.dealer.hand = PlayingCardPile()

        self.setup()

    def setup(self):
        # Init and draw 1 card for each player, then one for the dealer,
        # then another one for each player
        for player in self.players:
            player.hand = PlayingCardPile()
            player.hand.add(self.deck.take(1))

        self.dealer.hand.add(self.deck.take(1))

        for player in self.players:
            player.hand.add(self.deck.take(1))

        if self.debug:
            print("Dealer's first card : {}".format(self.dealer.hand))
            for player in self.players:
                print("Player '{}' 's initial hand : {}".format(player.name, str(player.hand)))

    def play_console(self):
        # Player drawing loop
        for player in self.players:
            choice = ""
            self._print_hand_and_score(player)
            while (self.eval_score(player.hand) < 21) and (choice not in ["stand"]):
                choice = input("What do you wanna do? (hit/stand) : ").lower()

                if choice == "hit":
                    player.hand.add(self.deck.take(1))
                    self._print_hand_and_score(player)

        # Dealer's 2nd card, then more draws while score under 17
        self.dealer.hand.add(self.deck.take(1))
        self._print_hand_and_score(self.dealer)

        while self.eval_score(self.dealer.hand) < 17:
            self.dealer.hand.add(self.deck.take(1))
            print("Dealer grabs another card...")
            self._print_hand_and_score(self.dealer)

        # TODO Check if players or dealer busted, to know who won or not

    def _print_hand_and_score(self, player):
        print("\nPlayer '{}', your hand is : {}".format(player.name, str(player.hand)))
        print("Your hand is worth {} points".format(self.eval_score(player.hand)))

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
