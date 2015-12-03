"""
Tests for Advent of Code
"""

import day1, day2


def test_day_1():
    version = day1.find_santas_floor_v3
    assert day1.find_santas_floor('(())', version=version) == 0
    assert day1.find_santas_floor('()()', version=version) == 0
    assert day1.find_santas_floor('(((', version=version) == 3
    assert day1.find_santas_floor('(()(()(', version=version) == 3
    assert day1.find_santas_floor('))(((((', version=version) == 3
    assert day1.find_santas_floor('())', version=version) == -1
    assert day1.find_santas_floor('))(', version=version) == -1
    assert day1.find_santas_floor(')))', version=version) == -3
    assert day1.find_santas_floor(')())())', version=version) == -3

    assert day1.basement_entrance(')') == 1
    assert day1.basement_entrance('()())') == 5

def test_day_2():
    assert day2.order_paper(['2x3x4']) == 58
    assert day2.order_paper(['1x1x10']) == 43
    assert day2.order_paper(['2x3x4', '1x1x10']) == 58 + 43

    assert day2.order_ribbons(['2x3x4']) == 34
    assert day2.order_ribbons(['1x1x10']) == 14
    assert day2.order_ribbons(['2x3x4', '1x1x10']) == 34 + 14

