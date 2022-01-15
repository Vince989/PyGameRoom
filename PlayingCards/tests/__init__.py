# -*- coding: utf-8 -*-
from ..PlayingCard import PlayingCard, \
    SUIT_CLUBS, RANK_10, SUIT_SPADES, RANK_A, \
    SUIT_HEARTS, RANK_QUEEN, SUIT_DIAMONDS, RANK_2


def make_10_of_clubs():
    return PlayingCard(SUIT_CLUBS, RANK_10)


def make_ace_of_spades():
    return PlayingCard(SUIT_SPADES, RANK_A)


def make_queen_of_hearts():
    return PlayingCard(SUIT_HEARTS, RANK_QUEEN)


def make_2_of_diamonds():
    return PlayingCard(SUIT_DIAMONDS, RANK_2)
