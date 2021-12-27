# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack


def test_blackjack():
    blackjack = Blackjack(2)
    assert blackjack.hands  # TODO Make better checks
