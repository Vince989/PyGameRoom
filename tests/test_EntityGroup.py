# -*- coding: utf-8 -*-
from src.EntityGroup import EntityGroup
from src.Entity import Entity


def test_entitygroup_init():
    entity_group = EntityGroup()
    assert entity_group

    assert entity_group.shuffle() is None  # A pass-through, should work but return nothing


def test_add():
    entity_group = EntityGroup()
    amount = 5
    for i in range(amount):  # Generate (amount) items
        new_entity = Entity()
        entity_group.add(new_entity)

    assert len(entity_group.items) == amount


def test_take():
    entity_group = EntityGroup()

    amount = 5
    take = 3
    assert take <= amount

    for i in range(amount):  # Generate (amount) items
        new_entity = Entity()
        entity_group.add(new_entity)

    taken = []
    for j in range(take):
        taken.append(entity_group.take())

    assert len(taken) == take
    assert len(entity_group.items) == amount - take
