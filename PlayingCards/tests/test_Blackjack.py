# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack


def test_blackjack():
    players = 2
    blackjack = Blackjack(players)
    assert len(blackjack.players) == players  # TODO Make better checks
    assert blackjack.dealer.name == Blackjack.DEALER_NAME


def test_eval_score():
    pass
    # TODO
