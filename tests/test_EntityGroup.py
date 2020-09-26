# -*- coding: utf-8 -*-
from ..EntityGroup import EntityGroup


# noinspection PyPep8Naming
def test_EntityGroup():
    entity_group = EntityGroup()
    assert entity_group

    assert entity_group.shuffle() is None  # Loopback should work but return nothing
