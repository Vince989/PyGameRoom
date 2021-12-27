# -*- coding: utf-8 -*-
from ..Entity import Entity

# Unicode characters from : https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
SUIT_CLUBS = "♧"  # ♣ ♧
SUIT_DIAMONDS = "♦"  # ♦ ♢
SUIT_HEARTS = "♥"  # ♥ ♡
SUIT_SPADES = "♤"  # ♠ ♤
SUIT_NONE = ""
SUITS_LIST = [SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES]

RANK_A = "A"
RANK_2 = "2"
RANK_3 = "3"
RANK_4 = "4"
RANK_5 = "5"
RANK_6 = "6"
RANK_7 = "7"
RANK_8 = "8"
RANK_9 = "9"
RANK_10 = "10"
RANK_JACK = "J"
RANK_QUEEN = "Q"
RANK_KING = "K"
RANK_NONE = ""

STD_RANKS_FACES = [RANK_JACK, RANK_QUEEN, RANK_KING, ]
STD_RANKS_SEQUENCE = [RANK_A, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7, RANK_8, RANK_9,
                      RANK_10, RANK_JACK, RANK_QUEEN, RANK_KING, ]


class PlayingCard(Entity):
    def __init__(self, suit=SUIT_NONE, rank=RANK_NONE, joker_id=0, visible=True):
        """
        French-style playing cards

        :param str suit: Spades, clubs, etc.
        :param str rank: A, 2, ... 9, 10, J, Q, K
        :param int joker_id: If the card is a Joker, which number it is, otherwise 0
        :param bool visible: If the card is visible to others
        """
        super().__init__()

        self.suit = suit
        self.rank = rank
        self.joker_id = joker_id
        self.visible = visible

    def __repr__(self):  # pragma: no cover
        if self.joker_id:
            return "Joker #" + str(self.joker_id)
        else:
            return self.suit + " " + self.rank
