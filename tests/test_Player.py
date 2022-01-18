# -*- coding: utf-8 -*-
from Player import Player


def test_player_init():
    player_name = "THIS_IS_A_TEST"
    player = Player(player_name)
    assert player.name == player_name
    assert player.active


def test_wagers():
    init_p1 = 123
    init_p2 = 456
    bet1 = 13
    bet2 = 34
    player1 = Player("P1", init_p1)
    player2 = Player("P2", init_p2)

    player1.wager(bet1)
    player1.claim_bet()
    assert player1.cash == init_p1 + bet1

    player1.wager(bet2)
    player2.cash += player1.lose_bet()
    assert player2.cash == init_p2 + bet2
