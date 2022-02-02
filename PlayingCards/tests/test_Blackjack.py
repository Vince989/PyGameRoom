# -*- coding: utf-8 -*-
from ..Blackjack import Blackjack
from ..PlayingCardsPlayer import PlayingCardsPlayer
from ..PlayingCardPile import PlayingCardPile
from ..PlayingCard import PlayingCard, \
    SUIT_DIAMONDS, RANK_2, SUIT_SPADES, RANK_A, \
    SUIT_CLUBS, RANK_10, SUIT_HEARTS, RANK_QUEEN

NUM_PLAYERS = 2


def test_blackjack_init():
    players = NUM_PLAYERS
    blackjack = Blackjack(num_players=players)
    assert len(blackjack.players) == players
    assert blackjack.dealer.name == Blackjack.DEALER_NAME


def test_blackjack_setup():
    players = NUM_PLAYERS
    blackjack = Blackjack(num_players=players)
    blackjack.setup()
    assert len(blackjack.dealer.hand.items) == 2

    # Dealer's 2nd card shouldn't be visible at first
    assert not blackjack.dealer.hand.items[1].visible

    for player in range(players):
        assert len(blackjack.players[player].hand.items) == 2


def test_blackjack_play():
    players = NUM_PLAYERS
    blackjack = Blackjack(console=False, num_players=players)
    blackjack.setup()
    blackjack.dealer.hand = _bad_hand()  # Setup the base game, then override the dealer's hand
    blackjack.dealer.hand.items[1].visible = False
    assert not blackjack.dealer.hand.items[1].visible  # The 2nd card should be hidden

    blackjack.play()
    assert blackjack.dealer.hand.items[1].visible  # The 2nd card should be flipped now
    for player in blackjack.players:
        assert len(player.hand.items) == 2


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

    # ... Then the player busts!
    player.hand.add(PlayingCard(SUIT_DIAMONDS, RANK_2))
    player.hand.add(PlayingCard(SUIT_CLUBS, RANK_10))
    assert Blackjack.eval_score(player.hand) == 23


def test_dealer_wins():
    blackjack = Blackjack(num_players=2)
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
