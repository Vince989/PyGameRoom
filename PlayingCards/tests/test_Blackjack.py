# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack
from ..PlayingCardsPlayer import PlayingCardsPlayer
from ..PlayingCardPile import PlayingCardPile
from ..PlayingCard import PlayingCard, \
    SUIT_DIAMONDS, RANK_2, SUIT_SPADES, RANK_A, \
    SUIT_CLUBS, RANK_10, SUIT_HEARTS, RANK_QUEEN


def test_blackjack_init():
    players = 5
    blackjack = Blackjack(players)
    assert len(blackjack.players) == players
    assert blackjack.dealer.name == Blackjack.DEALER_NAME


def test_blackjack_setup():
    players = 2
    blackjack = Blackjack(players)
    blackjack.setup()

    assert len(blackjack.dealer.hand.items) == 2

    # Dealer's 2nd card shouldn't be visible at first
    assert not blackjack.dealer.hand.items[1].visible

    for player in range(players):
        assert len(blackjack.players[player].hand.items) == 2


def test_eval_score():
    player = PlayingCardsPlayer("TEST")  # Arbitrary name
    player.hand.add(PlayingCard(SUIT_DIAMONDS, RANK_2))
    player.hand.add(PlayingCard(SUIT_SPADES, RANK_A))
    assert Blackjack.eval_score(player.hand) == 13  # 2 + 11
    player.hand.add(PlayingCard(SUIT_CLUBS, RANK_10))
    assert Blackjack.eval_score(player.hand) == 13  # 2 + 11 + 10 ... wait, 2 + 1 + 10

    player = PlayingCardsPlayer("TEST2")  # Arbitrary name, again
    player.hand.add(PlayingCard(SUIT_SPADES, RANK_A))
    player.hand.add(PlayingCard(SUIT_HEARTS, RANK_QUEEN))
    assert Blackjack.eval_score(player.hand) == 21  # Blackjack case


def test_dealer_wins():
    blackjack = Blackjack(2)
    blackjack.dealer.hand = _blackjack_hand()

    blackjack.players[0].hand = _bad_hand()
    blackjack.players[1].hand = _bad_hand()

    assert not blackjack._player_won(blackjack.players[0])
    assert not blackjack._player_won(blackjack.players[1])


# UTILITY FUNCTIONS

def _blackjack_hand():
    """ Worth 21 """
    hand = PlayingCardPile()
    hand.add(PlayingCard(suit=SUIT_SPADES, rank=RANK_A))
    hand.add(PlayingCard(suit=SUIT_CLUBS, rank=RANK_10))
    return hand


def _bad_hand():
    """ Worth 12 """
    hand = PlayingCardPile()
    hand.add(PlayingCard(suit=SUIT_HEARTS, rank=RANK_2))
    hand.add(PlayingCard(suit=SUIT_DIAMONDS, rank=RANK_QUEEN))
    return hand
