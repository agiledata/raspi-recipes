# -*- coding: utf-8 -*-
# recipes/pi_traffic.py

"""
Recipe for using PiTraffic
"""

from recipes.hardware import Hardware


class Light(Hardware):

    def __init__(self, color):
        self.color = color
        self._state = 'off'

    def on(self):
        self._state = 'on'

    def off(self):
        self._state = 'off'

# green = Light('green')
#
#
# __all__ = ['green']

