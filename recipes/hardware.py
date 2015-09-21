# -*- coding: utf-8 -*-
# recipes/hardware.py

__metaclass__ = object  #  If Python 2 then use new-style class.


class Hardware:

    def help(self):
        return "This should be some help"

    def learn(self):
        yield('stage_1')
        yield('stage_2')
        yield('stage_3')
        yield('stage_4')

    def reset(self):
        """Reset to factory settings"""

    def test(self):
        """Make the hardware work, visibly"""


