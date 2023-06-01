# -*- coding: utf-8 -*-
from src.PyGameRoom.Cards.PlayingCard import \
    PlayingCard, SUIT_NONE, RANK_NONE, HIDDEN, \
    SUIT_CLUBS, RANK_10, RANK_A, SUIT_SPADES
from src.PyGameRoom.ConsoleColors import ConsoleColors


def test_playingcard_init():
    # Create and test a few cards...
    card = PlayingCard(SUIT_CLUBS, RANK_10, visible=False)
    assert card.suit == SUIT_CLUBS
    assert card.rank == RANK_10
    assert card.joker_id == 0
    assert str(card) == f"{HIDDEN}"
    card.visible = True
    assert str(card) == f"{RANK_10} {SUIT_CLUBS}{ConsoleColors.ENDC}"

    card = PlayingCard(SUIT_SPADES, RANK_A, visible=True)
    assert card.suit == SUIT_SPADES
    assert card.rank == RANK_A
    assert card.joker_id == 0
    assert str(card) == f"{ConsoleColors.GREEN}A {SUIT_SPADES}{ConsoleColors.ENDC}"

    # TODO Test more card ranks and suites

    # Create and test the first joker
    card = PlayingCard(joker_id=1, visible=True)
    assert card.suit == SUIT_NONE
    assert card.rank == RANK_NONE
    assert card.joker_id == 1
    assert str(card) == "Joker #1"
