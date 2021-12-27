# -*- coding: utf-8 -*-
from random import shuffle


class EntityGroup(object):
    def __init__(self):
        """
        For general/generic functionality across groups of objects
        """
        self.items = []

    def shuffle(self):
        """
        "Loop-back" to enable shuffling the current set

        :return: a None
        """
        return shuffle(self.items)

    def take(self, amount=1):
        stack = []
        for i in range(amount):
            stack.append(self.items.pop())

        return stack

    # To complete as needed...
