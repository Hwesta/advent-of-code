"""
Tests for Advent of Code
"""
from . import day1, day2, day3, day4


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

def test_day_4():
    assert day4.real_room('aaaaa-bbb-z-y-x', 'abxyz') is True
    assert day4.real_room('a-b-c-d-e-f-g-h', 'abcde') is True
    assert day4.real_room('not-a-real-room', 'oarel') is True
    assert day4.real_room('totally-real-room', 'decoy') is False

    assert day4.solve([
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]) == 1514

    assert day4.rotate_room('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'
