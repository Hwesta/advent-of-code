"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2

@pytest.mark.parametrize('seq,sum,halfway', [
    ('1122', 3, False),
    ('1111', 4, False),
    ('1234', 0, False),
    ('91212129', 9, False),
    ('1212', 6, True),
    ('1221', 0, True),
    ('123425', 4, True),
    ('123123', 12, True),
    ('12131415', 4, True),
])
def test_day_1(seq, sum, halfway):
    assert day1.solve(seq, halfway=halfway) == sum

@pytest.mark.parametrize('sheet,checksum,modulo', [
    ('''5 1 9 5
7 5 3
2 4 6 8''', 18, False),
    ('''5 9 2 8
9 4 7 3
3 8 6 5''', 9, True),
])
def test_day_2(sheet, checksum,modulo):
    assert day2.solve(sheet, modulo=modulo) == checksum
