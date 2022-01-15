# -*- coding: utf-8 -*-
from ..PlayingCard import PlayingCard, SUIT_NONE, RANK_NONE, \
    SUIT_CLUBS, RANK_10, RANK_A, SUIT_SPADES
from . import make_10_of_clubs, make_ace_of_spades


# noinspection PyPep8Naming
def test_PlayingCard():
    # Create and test a 5 of clubs
    card = make_10_of_clubs()
    assert card.suit == SUIT_CLUBS
    assert card.rank == RANK_10
    assert card.joker_id == 0

    card = make_ace_of_spades()
    assert card.suit == SUIT_SPADES
    assert card.rank == RANK_A
    assert card.joker_id == 0

    # Create and test the first joker
    card = PlayingCard(joker_id=1)
    assert card.suit == SUIT_NONE
    assert card.rank == RANK_NONE
    assert card.joker_id == 1
