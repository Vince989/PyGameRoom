# -*- coding: utf-8 -*-
from ..Entity import Entity


class Card(Entity):
    def __init__(self, visible=False):
        """
        A generic card, can be french playing card, uno, skip bo, etc.

        :param bool visible: If the card is visible to others (face up?)
        """
        super().__init__(visible)
