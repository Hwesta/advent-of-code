"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3, day4, day5, day6, day7, day8

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
def test_day_2(sheet, checksum, modulo):
    assert day2.solve(sheet, modulo=modulo) == checksum


@pytest.mark.parametrize('data,answer,flag', [
    ('1', 0, False),
    ('12', 3, False),
    ('23', 2, False),
    ('1024', 31, False),
    ('7', 10, True),
    ('800', 806, True),
])
def test_day_3(data, answer, flag):
    assert day3.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ('aa bb cc dd ee', 1, False),
    ('aa bb cc dd aa', 0, False),
    ('aa bb cc dd aaa', 1, False),
    ('abcde fghij', 1, True),
    ('abcde xyz ecdab', 0, True),
    ('a ab abc abd abf abj', 1, True),
    ('iiii oiii ooii oooi oooo', 1, True),
    ('oiii ioii iioi iiio', 0, True),
])
def test_day_4(data, answer, flag):
    assert day4.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ('''0
3
0
1
-3''', 5, False),
    ('''0
3
0
1
-3''', 10, True),
])
def test_day_5(data, answer, flag):
    assert day5.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ('''0	2	7	0''', 5, False),
    ('''0   2   7   0''', 4, True),
])
def test_day_6(data, answer, flag):
    assert day6.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ('''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)''', 'tknk', False),
    ('''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)''', 60, True),
])
def test_day_7(data, answer, flag):
    assert day7.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ('''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10''', 1, False),
])
def test_day_8(data, answer, flag):
    assert day8.solve(data, flag) == answer
