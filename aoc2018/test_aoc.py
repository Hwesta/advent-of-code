"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1


@pytest.mark.parametrize(
    "data,answer,flag",
    [
        (["+1", "+1", "+1"], 3, False),
        (["0", "+1"], 1, False),
        (["-1", "+3"], 2, False),
        (["+1", "-1"], 0, True),
        (["+3", "+3", "+4", "-2", "-4"], 10, True),
        (["-6", "+3", "+8", "+5", "-6"], 5, True),
        (["+7", "+7", "-2", "-7", "-4"], 14, True),
    ],
)
def test_day_1(data, answer, flag):
    assert day1.solve(data, flag) == answer
