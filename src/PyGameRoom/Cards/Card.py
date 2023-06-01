# -*- coding: utf-8 -*-
from ..Entity import Entity
# from .PlayingCard import PlayingCard, STD_RANKS_SEQUENCE, SUITS_LIST


class Card(Entity):
    def __init__(self, visible=False):
        """
        French-style playing cards

        :param bool visible: If the card is visible to others (face up?)
        """
        super().__init__(visible)
