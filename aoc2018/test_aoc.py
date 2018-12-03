"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3


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

@pytest.mark.parametrize('data,answer,flag', [
    (["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"], 12, False),
    (["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"], "fgij", True)
])
def test_day_2(data, answer, flag):
    assert day2.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    (["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 4, False),
    (["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 3, True),
])
def test_day_3(data, answer, flag):
    assert day3.solve(data, flag) == answer
