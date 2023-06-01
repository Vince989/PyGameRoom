# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name, cash=100):
        """
        Whichever game is played, this is where Players come from! ;)

        :param str name: The player's name
        :param int cash: How much money/tokens the Player has
        """
        self.name = name
        self.cash = cash

        self.active = True  # Basically, dead or alive.
        self.bet = 0  # The Player's current bet

    def wager(self, amount):
        """
        Sets the Player's wager

        :param amount: The amount wager-ed
        """
        self.bet = amount
        self.cash -= self.bet

    def claim_bet(self):
        """
        The Player won, therefore gets his wager back, and its value a second time
        """
        self.cash += (self.bet * 2)  # Gain your tokens from the table, and then what you won
        self.bet = 0

    def lose_bet(self):
        """
        When a Player loses its bet

        :return: The amount the Player lost
        """
        bet = self.bet
        self.bet = 0
        return bet
