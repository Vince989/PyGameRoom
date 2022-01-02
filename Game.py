# -*- coding: utf-8 -*-
from Player import Player


class Game(object):
    def __init__(self, num_players=1):
        self.players = []
        for player in range(num_players):
            self.players.append(Player(player))  # Its index as a name by default
