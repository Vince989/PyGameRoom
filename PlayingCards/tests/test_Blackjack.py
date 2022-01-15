# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack
from ..PlayingCardsPlayer import PlayingCardsPlayer
from . import make_2_of_diamonds, make_10_of_clubs, \
    make_ace_of_spades, make_queen_of_hearts


def test_blackjack():
    players = 5
    blackjack = Blackjack(players)
    assert len(blackjack.players) == players  # TODO Make better checks
    assert blackjack.dealer.name == Blackjack.DEALER_NAME


def test_eval_score():
    player = PlayingCardsPlayer("TEST")  # Arbitrary name
    player.hand.add(make_2_of_diamonds())
    player.hand.add(make_ace_of_spades())
    assert Blackjack.eval_score(player.hand) == 13  # 2 + 11
    player.hand.add(make_10_of_clubs())
    assert Blackjack.eval_score(player.hand) == 13  # 2 + 11 + 10 ... wait, 2 + 1 + 10

    player = PlayingCardsPlayer("TEST2")  # Arbitrary name, again
    player.hand.add(make_ace_of_spades())
    player.hand.add(make_queen_of_hearts())
    assert Blackjack.eval_score(player.hand) == 21  # Blackjack case
