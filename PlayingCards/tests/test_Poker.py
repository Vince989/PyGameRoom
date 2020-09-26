# -*- coding: utf-8 -*-
from ..Poker import Poker


def test_poker():
    poker = Poker(2)
    assert poker.hands  # TODO Make better checks?
