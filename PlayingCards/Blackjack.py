# -*- coding: utf-8 -*-
from Game import Game
from .PlayingCardsPlayer import PlayingCardsPlayer
from .PlayingCardPile import PlayingCardPile
from .PlayingCard import RANK_A


class Blackjack(Game):
    DEALER_NAME = "DEALER"  # Yeah, he's a pretty cool dude!

    def __init__(self, num_players=1, decks=6):
        """
        Blackjack, with a Dealer playing with N players

        :param int num_players: Number of players
        """
        super().__init__()

        # Supposed to be always 6 decks in Blackjack ??
        self.deck = PlayingCardPile(full_decks=decks)
        self.deck.shuffle()

        self.dealer = PlayingCardsPlayer(self.DEALER_NAME)

        # Init all players
        for player in range(num_players):
            self.players.append(PlayingCardsPlayer(str(player)))

    def setup(self):
        # Draw 1 card for each player,
        for player in self.players:
            player.hand.add(self.deck.take(1))

        # ... then one for the dealer,
        self.dealer.hand.add(self.deck.take(1))

        # ... then another 1 for each player,
        for player in self.players:
            player.hand.add(self.deck.take(1))

        # ... and finally a hidden one for the dealer
        self.dealer.hand.add(self.deck.take(1, visible=False))

        # Print() the initial hands
        print("Dealer's first cards : {}".format(str(self.dealer.hand)))
        for player in self.players:
            print("Player '{}' 's initial hand : {}".format(player.name, str(player.hand)))

    def play(self):
        # Ask every player if they want more cards (hit), or to "stand" in place
        for player in self.players:
            choice = ""
            self._print_hand_and_score(player)
            player_score = self.eval_score(player.hand)

            while (player_score < 21) and (choice not in ["stand"]):
                choice = input("What do you wanna do? (hit/stand) : ").lower()
                if choice == "hit":
                    player.hand.add(self.deck.take(1))
                    self._print_hand_and_score(player)
                    player_score = self.eval_score(player.hand)

                    if player_score == 0:
                        player.active = False
                        print("Player '{}' BUSTED.".format(player.name))

            if player_score == 21:  # Blackjack or equivalent
                print("Player '{}' will WIN, 21, baby!".format(player.name))

        # Then flip over dealer's 2nd card,
        self.dealer.hand.items[1].visible = True
        self._print_hand_and_score(self.dealer)

        # ... and then draw more cards while its score is under 17
        while self.eval_score(self.dealer.hand) < 17:
            print("Dealer grabs another card...")
            self.dealer.hand.add(self.deck.take(1))
            self._print_hand_and_score(self.dealer)

    def finish(self):
        # Check if the dealer busted, then the players, to know who won or lost
        dealer_final_score = self.eval_score(self.dealer.hand)

        if dealer_final_score > 21:
            self.dealer.active = False
            print("\nDealer busted, all remaining players win!\n")
        else:
            print("\nDealer didn't bust, let's see who won...\n")

        for player in self.players:
            if self._player_won(player):
                print("Player '{}' wins with {} points! {}".format(
                      player.name, self.eval_score(player.hand), player.hand))
            else:
                print("Player '{}' loses at {} points... {}".format(
                      player.name, self.eval_score(player.hand), player.hand))

    def _player_won(self, player):
        """
        For a win in Blackjack, the player must not have busted,
        and either have a higher score than the Dealer, or the Dealer has busted

        :param PlayingCardsPlayer player: a Blackjack Player
        :return: if said player won against the Dealer
        :rtype: bool
        """
        return player.active and \
            (not self.dealer.active or
             self.eval_score(player.hand) >= self.eval_score(self.dealer.hand))

    def _print_hand_and_score(self, player):  # pragma: no cover
        print("\nPlayer '{}', you have {} tokens, and your hand is : {}".format(
              player.name, player.cash, str(player.hand)))
        print("Your hand is worth {} points.".format(self.eval_score(player.hand)))

    @staticmethod
    def eval_score(player):
        score = 0
        aces = 0
        tens = 0

        # Remember it if there's at least an Ace, and "ceil off" the Faces
        for card in player.items:
            if card.rank == RANK_A:
                aces += 1
            if card.rank >= 10:
                card.rank = 10
                tens += 1
            score += card.rank

        if len(player.items) == 2 and aces and tens:  # Blackjack!
            score = 21
        elif aces and score < 11:  # Add the Ace value if there's room
            score += 10

        return score
