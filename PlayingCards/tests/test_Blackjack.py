# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack
from ..PlayingCardsPlayer import PlayingCardsPlayer
from ..PlayingCard import PlayingCard, \
    SUIT_DIAMONDS, RANK_2, SUIT_SPADES, RANK_A, \
    SUIT_CLUBS, RANK_10, SUIT_HEARTS, RANK_QUEEN


def test_blackjack():
    players = 5
    blackjack = Blackjack(players)
    assert len(blackjack.players) == players  # TODO Make better checks
    assert blackjack.dealer.name == Blackjack.DEALER_NAME


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
