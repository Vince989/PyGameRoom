# -*- coding: utf-8 -*-
from random import shuffle


class EntityGroup(object):
    def __init__(self):
        """
        For general/generic functionality across groups of objects
        """
        self.items = []

    def __str__(self):
        # Could be more python-ic probably ?
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
        """
        Remove some entities from this group

        :param int amount: Number of entities to take (pop)
        :return: The removed entities
        """
        entities = []
        for i in range(amount):
            entities.append(self.items.pop())

        return entities

    def add(self, new_items):
        """
        Add/append entities to this group

        :param new_items: List of entities to add
        :return: None
        """
        for item in new_items:
            self.items.append(item)
