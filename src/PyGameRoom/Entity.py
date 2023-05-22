# -*- coding: utf-8 -*-


class Entity(object):
    def __init__(self, visible=True):
        """
        For shared functionality across cards/pieces/etc

        :param bool visible: If the entity should be visible to all
        """
        self.visible = visible
