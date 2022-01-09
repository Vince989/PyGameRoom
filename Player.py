# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name):
        """
        Whichever game is played, this is where Players come from! ;)

        :param str name: The player's name
        """
        self.name = name
        self.active = True  # Basically, dead or alive.
