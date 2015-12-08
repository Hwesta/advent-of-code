"""
Tests for Advent of Code
"""

import day1, day2, day3, day4, day5, day6, day7, day8


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

def test_day_3():
    assert day3.delivered_houses('>') == 2
    assert day3.delivered_houses('^>v<') == 4
    assert day3.delivered_houses('^v^v^v^v^v') == 2

    assert day3.delivered_houses_with_robot('^v') == 3
    assert day3.delivered_houses_with_robot('^>v<') == 3
    assert day3.delivered_houses_with_robot('^v^v^v^v^v') == 11

def test_day_4():
    assert day4.generate_advent_coins('abcdef') == 609043
    assert day4.generate_advent_coins('pqrstuv') == 1048970

def test_day_5():
    assert day5.nice_strings(['ugknbfddgicrmopn']) == 1
    assert day5.nice_strings(['aaa']) == 1
    assert day5.nice_strings(['jchzalrnumimnmhp']) == 0
    assert day5.nice_strings(['haegwjzuvuyypxyu']) == 0
    assert day5.nice_strings(['dvszwmarrgswjxmb']) == 0

    assert day5.better_nice_strings(['qjhvhtzxzqqjkmpb']) == 1
    assert day5.better_nice_strings(['xxyxx']) == 1
    assert day5.better_nice_strings(['uurcxstgmygtbstg']) == 0
    assert day5.better_nice_strings(['ieodomkazucvgmuy']) == 0

def test_day_6():
    assert day6.winning_lights(['turn on 0,0 through 999,999']) == 1000000
    assert day6.winning_lights(['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0']) == 1000000 - 1000
    assert day6.winning_lights(['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500']) == 1000000 - 4

    assert day6.winning_lights_brightness(['turn on 0,0 through 0,0']) == 1
    assert day6.winning_lights_brightness(['toggle 0,0 through 999,999']) == 2000000

def test_day_7():
    data = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    ret = day7.run_circuit(data)
    assert ret['x'] == 123
    assert ret['y'] == 456
    assert ret['d'] == 72
    assert ret['e'] == 507
    assert ret['f'] == 492
    assert ret['g'] == 114
    assert ret['i'] == -457  # Unsigned: 65079
    assert ret['h'] == -124  # Unsigned: 65412

def test_day_8():
    assert day8.wasted_space([r'""']) == 2
    assert day8.wasted_space([r'"abc"']) == 2
    assert day8.wasted_space([r'"aaa\"aaa"']) == 3
    assert day8.wasted_space([r'"\x27"']) == 5
    assert day8.wasted_space([
        r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'
    ]) == 12
    assert day8.encode_wasted_space([r'""']) == 4
    assert day8.encode_wasted_space([r'"abc"']) == 4
    assert day8.encode_wasted_space([r'"aaa\"aaa"']) == 6
    assert day8.encode_wasted_space([r'"\x27"']) == 5
    assert day8.encode_wasted_space([
        r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'
    ]) == 19
