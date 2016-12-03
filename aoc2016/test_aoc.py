"""
Tests for Advent of Code
"""
from . import day1, day2, day3


def test_day_1():
    assert day1.solve('R2, L3') == 5
    assert day1.solve('R2, R2, R2') == 2
    assert day1.solve('R5, L5, R5, R3') == 12

    assert day1.solve('R8, R4, R4, R8', dupe=True) == 4

def test_day_2():
    assert day2.solve("ULL\nRRDDD\nLURDL\nUUUUD") == '1985'
    assert day2.solve("ULL\nRRDDD\nLURDL\nUUUUD", big=True) == '5DB3'

    assert day2.solve_better("ULL\nRRDDD\nLURDL\nUUUUD") == '1985'
    assert day2.solve_better("ULL\nRRDDD\nLURDL\nUUUUD", big=True) == '5DB3'

def test_day_3():
    assert day3.solve(["  5  10 25 "]) == 0
    assert day3.solve(["  25  20 10 "]) == 1

    assert day3.solve_vertical(['2 2 2', '2 3 4', '1 1 1', '10 11 12', '5 5 5', '6 6 6']) == 2
