# -*- coding: utf-8 -*-
from random import shuffle


class EntityGroup(object):
    def __init__(self):
        """
        For general/generic functionality across groups of objects
        """
        self.items = []

    def __repr__(self):
        output = ""
        sep = ", "
        for item in self.items:
            output += str(item) + sep
        return output[:-len(sep)]

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

    def add(self, new_items):
        for item in new_items:
            self.items.append(item)

    # To complete as needed...
