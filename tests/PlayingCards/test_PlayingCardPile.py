# -*- coding: utf-8 -*-
from src.PlayingCards.PlayingCardPile import PlayingCardPile


def test_playingcardpile_init():
    # Test creating various card piles
    deck_size = 13 * 4

    deck = PlayingCardPile()
    assert len(deck.items) == 0  # should be an empty pile

    deck = PlayingCardPile(full_decks=0)
    assert len(deck.items) == 0  # should be an empty pile too

    deck = PlayingCardPile(full_decks=1)
    assert len(deck.items) == deck_size  # should be 52 items

    deck = PlayingCardPile(full_decks=1, jokers=2)
    assert len(deck.items) == deck_size + 2  # should be 54 items

    deck = PlayingCardPile(full_decks=2)
    assert len(deck.items) == (deck_size * 2)  # should be 104 items

    deck = PlayingCardPile(full_decks=2, jokers=2)
    assert len(deck.items) == (deck_size * 2) + (2 * 2)  # should be 108 items

    assert deck.shuffle() is None  # Pass-through should work but return nothing
