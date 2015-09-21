# -*- coding: utf-8 -*-
# recipes/pi_traffic.py

"""
Recipe for using PiTraffic
"""

from recipes.hardware import Hardware


class Light(Hardware):

    def __init__(self, color):
        self.color = color


# green = Light('green')
#
#
# __all__ = ['green']

