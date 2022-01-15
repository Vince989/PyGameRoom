# -*- coding: utf-8 -*-
from ..EntityGroup import EntityGroup
from ..Entity import Entity


# noinspection PyPep8Naming
def test_EntityGroup():
    entity_group = EntityGroup()
    assert entity_group

    assert entity_group.shuffle() is None  # Pass-through should work but return nothing


def test_add():
    entity_group = EntityGroup()
    amount = 10
    for i in range(amount):  # Generate 10 items
        new_entity = Entity()
        entity_group.add(new_entity)
    assert len(entity_group.items) == amount


def test_take():
    entity_group = EntityGroup()
    amount = 10
    for i in range(amount):  # Generate 10 items
        new_entity = Entity()
        entity_group.add(new_entity)

    taken = []
    for j in range(3):
        taken.append(entity_group.take())
    assert len(taken) == 3
