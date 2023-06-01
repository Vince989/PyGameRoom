# -*- coding: utf-8 -*-
from .Card import Card
from ..ConsoleColors import ConsoleColors

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
STD_RANKS_SEQUENCE = [RANK_A, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7,
                      RANK_8, RANK_9, RANK_10, RANK_JACK, RANK_QUEEN, RANK_KING, ]


class PlayingCard(Card):
    def __init__(self, suit=SUIT_NONE, rank=RANK_NONE, joker_id=0, visible=False):
        """
        French-style playing cards

        :param str suit: Spades, clubs, hearts, diamonds
        :param str rank: A, 2, ... 9, 10, J, Q, K , or NONE
        :param int joker_id: If the card is a Joker, which "number" it is, otherwise 0
        :param bool visible: If the card is visible to others (face up)
        """
        super().__init__(visible)

        self.suit = suit
        self.rank = rank
        self.joker_id = joker_id

    def __str__(self):  # pragma: no cover
        color = ""
        if self.visible:
            if self.joker_id:
                return "Joker #" + str(self.joker_id)
            else:
                if self.rank == RANK_JACK:
                    rank = "J"
                elif self.rank == RANK_QUEEN:
                    rank = "Q"
                elif self.rank == RANK_KING:
                    rank = "K"
                elif self.rank == RANK_A:
                    rank = "A"
                else:
                    rank = str(self.rank)

                # if self.suit in SUIT_COLOR_RED:
                if self.suit is SUIT_HEARTS:
                    color = ConsoleColors.RED
                elif self.suit is SUIT_DIAMONDS:
                    color = ConsoleColors.BLUE
                elif self.suit is SUIT_SPADES:
                    color = ConsoleColors.GREEN

                return color + rank + " " + self.suit + ConsoleColors.ENDC
        else:
            return "(hidden)"
