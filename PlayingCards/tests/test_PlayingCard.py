# -*- coding: utf-8 -*-
from ..PlayingCard import PlayingCard, SUIT_CLUBS, RANK_5


# noinspection PyPep8Naming
def test_PlayingCard():
    # Create and test a 5 of clubs
    card = PlayingCard(SUIT_CLUBS, RANK_5)
    assert card.suit == SUIT_CLUBS
    assert card.rank == RANK_5
    assert card.joker_id == 0

    # Create and test the first joker
    card = PlayingCard(joker_id=1)
    assert card.suit == ""  # Meaning none
    assert card.rank == ""  # Meaning none
    assert card.joker_id == 1
