# -*- coding: utf-8 -*-
from Entity import Entity

# Unicode characters from : https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
SUIT_CLUBS = "♧"  # ♣ ♧
SUIT_DIAMONDS = "♦"  # ♦ ♢
SUIT_HEARTS = "♥"  # ♥ ♡
SUIT_SPADES = "♤"  # ♠ ♤
SUIT_NONE = ""
SUIT_COLOR_RED = [SUIT_HEARTS, SUIT_DIAMONDS]
SUIT_COLOR_BLACK = [SUIT_SPADES, SUIT_CLUBS]
SUITS_LIST = [SUIT_CLUBS, SUIT_DIAMONDS, SUIT_HEARTS, SUIT_SPADES]

RANK_A = 1
RANK_2 = 2
RANK_3 = 3
RANK_4 = 4
RANK_5 = 5
RANK_6 = 6
RANK_7 = 7
RANK_8 = 8
RANK_9 = 9
RANK_10 = 10
RANK_JACK = 11
RANK_QUEEN = 12
RANK_KING = 13
RANK_NONE = 0

STD_RANKS_FACES = [RANK_JACK, RANK_QUEEN, RANK_KING, ]
STD_RANKS_SEQUENCE = [RANK_A, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7, RANK_8, RANK_9,
                      RANK_10, RANK_JACK, RANK_QUEEN, RANK_KING, ]


class PlayingCard(Entity):
    def __init__(self, suit=SUIT_NONE, rank=RANK_NONE, joker_id=0, visible=False):
        """
        French-style playing cards

        :param str suit: Spades, clubs, hearts, diamonds
        :param str rank: A, 2, ... 9, 10, J, Q, K
        :param int joker_id: If the card is a Joker, which "number" it is, otherwise 0
        :param bool visible: If the card is visible to others (face up)
        """
        super().__init__(visible)

        self.suit = suit
        self.rank = rank
        self.joker_id = joker_id

    def __str__(self):  # pragma: no cover
        if self.visible:
            if self.joker_id:
                return "Joker #" + str(self.joker_id)
            else:
                if self.rank == 11:
                    rank = "J"
                elif self.rank == 12:
                    rank = "Q"
                elif self.rank == 13:
                    rank = "K"
                elif self.rank == 1:
                    rank = "A"
                else:
                    rank = str(self.rank)
                return rank + " " + self.suit
        else:
            return "(face down)"
