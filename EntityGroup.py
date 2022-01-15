# -*- coding: utf-8 -*-
from random import shuffle


class EntityGroup(object):
    def __init__(self):
        """
        For general/generic functionality across groups of objects
        """
        self.items = []

    def __str__(self):  # pragma: no cover
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

    def take(self, amount=1, visible=True):
        """
        Take/remove some entities from this group

        :param int amount: Amount of entities to take ("pop")
        :param bool visible: If the entities will become visible to all
        :return: The removed entities
        """
        entities = []
        for i in range(amount):
            entity = self.items.pop()
            entity.visible = visible
            entities.append(entity)

        return entities

    def add(self, new_items):
        """
        Add/append entities to this group

        :param new_items: List (or not) of entities to add
        :return: None
        """
        # Make the input a list, if it's not one already
        if not isinstance(new_items, list):
            new_items = [new_items]

        for item in new_items:
            self.items.append(item)
