# -*- coding: utf-8 -*-
from Player import Player
from .PlayingCardPile import PlayingCardPile


class PlayingCardsPlayer(Player):
    def __init__(self, name):
        """
        A Player playing a cards game.

        :param str name: The player's name
        """
        super().__init__(name)

        self.hand = PlayingCardPile()
