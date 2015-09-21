# -*- coding: utf-8 -*-
# recipes/tests/test_pi_traffic.py

import pytest

from recipes.pi_traffic import Light

xfail = pytest.mark.xfail
skipif = pytest.mark.skipif


def test_make_light():
    green_light = Light('green')
    assert green_light.color == 'green'
    # assert 0, 44
