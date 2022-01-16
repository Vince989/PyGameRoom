# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name, cash=1):
        """
        Whichever game is played, this is where Players come from! ;)

        :param str name: The player's name
        :param int cash: How much money/tokens the Player has
        """
        self.name = name
        self.active = True  # Basically, dead or alive.
        self.cash = cash

        self.bet = 0  # The Player's current bet

    def wager(self, amount):
        self.bet = amount
        self.cash -= self.bet

    def claim_bet(self):
        self.cash += self.bet
        self.bet = 0

    def lose_bet(self):
        bet = self.bet
        self.bet = 0
        return bet
