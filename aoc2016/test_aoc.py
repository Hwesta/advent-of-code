"""
Tests for Advent of Code
"""
import day1

def test_day_1():
    assert day1.solve('R2, L3') == 5
    assert day1.solve('R2, R2, R2') == 2
    assert day1.solve('R5, L5, R5, R3') == 12

    assert day1.solve('R8, R4, R4, R8', dupe=True) == 4
