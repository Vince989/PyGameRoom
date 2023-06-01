# -*- coding: utf-8 -*-
from src.PyGameRoom.Game import Game
from src.PyGameRoom.Cards.PlayingCardsPlayer import PlayingCardsPlayer
from src.PyGameRoom.Cards.PlayingCardPile import PlayingCardPile
from src.PyGameRoom.Cards.PlayingCard import RANK_A


class Blackjack(Game):
    DEALER_NAME = "DEALER"  # Yeah, he's a pretty cool dude!
    DEALER_DRAW_LIMIT = 17
    MAX_SCORE = 21

    def __init__(self, console=True, num_players=1, decks=6):
        """
        Blackjack, with a Dealer playing with N players

        :param bool console: Console mode or graphical
        :param int num_players: Number of players
        :param int decks: Number of card decks to be shuffled in the "heel"
        """
        super().__init__()

        self.console = console

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

    def play(self):
        # PLAYERS' PART #
        if self.console:
            # Print() the initial hands
            print("Dealer's first cards : {}".format(str(self.dealer.hand)))
            for player in self.players:
                print("Player '{}' 's initial hand : {}".format(player.name, str(player.hand)))

            # Ask every player if they want more cards (to hit), or to "stand" in place
            for player in self.players:
                self.console_player(player)
        else:
            pass  # TODO Do nothing for now, will be done later

        # DEALER'S PART #
        # Reveal the dealer's 2nd card,
        self.dealer.hand.items[1].visible = True
        if self.console:
            self._print_hand_and_score(self.dealer)

        # ... and then draw more cards while its score is under 17
        while self.eval_score(self.dealer.hand) < self.DEALER_DRAW_LIMIT:
            if self.console:
                input("Dealer grabs another card...")
            self.dealer.hand.add(self.deck.take(1))
            self._print_hand_and_score(self.dealer)

    def console_player(self, player):
        choice = ""
        self._print_hand_and_score(player)
        player_score = self.eval_score(player.hand)

        while (player_score < self.MAX_SCORE) and (choice not in ["stand"]):
            choice = input("What do you wanna do? (hit/stand) : ").lower()
            if choice == "hit":
                player.hand.add(self.deck.take(1))
                self._print_hand_and_score(player)
                player_score = self.eval_score(player.hand)

                if player_score > self.MAX_SCORE:
                    player.active = False
                    input("Player '{}' BUSTED.".format(player.name))

        if player_score == self.MAX_SCORE:  # Blackjack or equivalent
            input("Player '{}' will WIN, 21, baby!".format(player.name))

    def console_finish(self):
        # Check if the dealer busted, then the players, to know who won or lost
        if self.eval_score(self.dealer.hand) > self.MAX_SCORE:
            self.dealer.active = False
            input("\nDealer busted, all remaining players win!\n")
        else:
            input("\nDealer didn't bust, let's see who won...\n")

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
        if self.console:
            print("\nPlayer '{}', you have {} tokens, and your hand is : {}".format(
                    player.name, player.cash, str(player.hand)))
            print("Player '{}', your hand is worth {} points.".format(
                    player.name, self.eval_score(player.hand)))
        else:
            pass  # Might handle graphical status box here, TBD...

    @staticmethod
    def eval_score(player):
        score = 0
        aces = 0
        tens = 0

        # Remember it if there's at least an Ace, and "ceil off" the Faces' in the score counting
        for card in player.items:
            if card.rank == RANK_A:
                aces += 1

            if card.rank >= 10:
                score += 10
                tens += 1
            else:
                score += card.rank

        if len(player.items) == 2 and aces and tens:  # Blackjack!
            score = 21
        elif aces and score < 11:  # Add the Ace value if there's room
            score += 10

        return score
