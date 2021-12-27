# -*- coding: utf-8 -*-
from EntityGroup import EntityGroup
from .PlayingCard import PlayingCard, STD_RANKS_SEQUENCE, SUITS_LIST


class PlayingCardPile(EntityGroup):
    def __init__(self, full_decks=0, jokers=0):
        """
        A French-style playing card pile.

        Can be automatically filled with a number of decks, each having a number of Jokers.

        :param int full_decks: The amount of decks of 52 cards to generate
        :param int jokers: The amount of jokers to generate per deck
        """
        super().__init__()

        # Add X decks of base cards
        for times in range(full_decks):
            for suit in SUITS_LIST:
                for rank in STD_RANKS_SEQUENCE:
                    card = PlayingCard(suit=suit, rank=rank, visible=False)
                    self.items.append(card)

            # Add X jokers to the pile
            for joker in range(1, jokers+1):
                card = PlayingCard(joker_id=joker, visible=False)
                self.items.append(card)
