"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3, day4, day5, day6, day7, day8, day9
from . import day10, day11

@pytest.mark.parametrize('directions,distance,dupe', [
    ('R2, L3', 5, False),
    ('R2, R2, R2', 2, False),
    ('R5, L5, R5, R3', 12, False),
    ('R8, R4, R4, R8', 4, True),
])
def test_day_1(directions, distance, dupe):
    assert day1.solve(directions, dupe=dupe) == distance

@pytest.mark.parametrize('directions,code,big', [
    (["ULL", "RRDDD", "LURDL", "UUUUD"], '1985', False),
    (["ULL", "RRDDD", "LURDL", "UUUUD"], '5DB3', True),
])
def test_day_2(directions, code, big):
    assert day2.solve(directions, big=big) == code
    assert day2.solve_better(directions, big=big) == code

@pytest.mark.parametrize('edges,count', [
    (["  5  10 25 "], 0),
    (["  25  20 10 "], 1),
])
def test_day_3(edges, count):
    assert day3.solve(edges) == count

def test_day_3_vertical():
    assert day3.solve_vertical(['2 2 2', '2 3 4', '1 1 1', '10 11 12', '5 5 5', '6 6 6']) == 2

@pytest.mark.parametrize('room,checksum,answer', [
    ('aaaaa-bbb-z-y-x', 'abxyz', True),
    ('a-b-c-d-e-f-g-h', 'abcde', True),
    ('not-a-real-room', 'oarel', True),
    ('totally-real-room', 'decoy', False),
])
def test_day_4_real_room(room, checksum, answer):
    assert day4.real_room(room, checksum) == answer

def test_day_4():
    assert day4.solve([
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]) == 1514

    assert day4.rotate_room('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'


@unittest.skip("very slow")
def test_day_5():
    assert day5.solve('abc') == ('18f47a30', '05ace8e3')

@pytest.mark.parametrize('data', [
    ([
        'eedadn',
        'drvtee',
        'eandsr',
        'raavrd',
        'atevrs',
        'tsrnev',
        'sdttsa',
        'rasrtv',
        'nssdts',
        'ntnada',
        'svetve',
        'tesnvt',
        'vntsnd',
        'vrdear',
        'dvrsen',
        'enarar',
    ]),
])
def test_day_6(data):
    assert day6.solve(data) == 'easter'
    assert day6.solve(data, fewest=True) == 'advent'
    assert day6.solve_better(data) == 'easter'
    assert day6.solve_better(data, fewest=True) == 'advent'

@pytest.mark.parametrize('ip,valid', [
    ('abba[mnop]qrst', True),
    ('abcd[bddb]xyyx', False),
    ('aaaa[qwer]tyui', False),
    ('ioxxoj[asdfgh]zxcvbn', True),
])
def test_day_7_tls(ip, valid):
    assert day7.support_tls(ip) == valid

@pytest.mark.parametrize('ip,valid', [
    ('aba[bab]xyz', True),
    ('xyx[xyx]xyx', False),
    ('aaa[kek]eke', True),
    ('zazbz[bzb]cdb', True),
    ('aaa[aaa]aba', False)
])
def test_day_7_ssl(ip, valid):
    assert day7.support_ssl(ip) == valid

def test_day_7():
    data = [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn',
        'itgslvpxoqqakli[arktzcssgkxktejbno]wsgkbwwtbmfnddt[zblrboqsvezcgfmfvcz]iwyhyatqetsreeyhh'

    ]
    assert day7.solve(data) == 2

    data = [
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb',
    ]
    assert day7.solve(data, ssl=True) == 3

def test_day_8_rectangle():
    assert day8.solve(['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1'], 7, 3) == 6

@pytest.mark.parametrize('data,length,version', [
    ('ADVENT', 6, 1),
    ('A(1x5)BC', 7, 1),
    ('(3x3)XYZ', 9, 1),
    ('(6x1)(1x3)A', 6, 1),
    ('X(8x2)(3x3)ABCY', 18, 1),
    ('ADVENT', 6, 2),
    ('A(1x5)BC', 7, 2),
    ('(3x3)XYZ', 9, 2),
    ('X(8x2)(3x3)ABCY', 20, 2),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920, 2),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445, 2),
])
def test_day_9(data, length, version):
    assert day9.solve(data, version=version) == length

def test_day_10():
    data = [
        'value 5 goes to bot 2',
        'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1',
        'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0 ',
        'value 2 goes to bot 2',
    ]
    assert day10.solve(data, comparing=[2, 5]) == '2'
    assert day10.solve(data) == 5*2*3

@pytest.mark.parametrize('elevator,valid', [
    ({'floor': 0, 'contains': []}, False),
    ({'floor': 0, 'contains': ['PM']}, True),
    ({'floor': 0, 'contains': ['PG']}, True),
    ({'floor': 0, 'contains': ['PM', 'CM']}, True),
    ({'floor': 0, 'contains': ['PG', 'CG']}, True),
    ({'floor': 0, 'contains': ['PG', 'PM']}, True),
    ({'floor': 0, 'contains': ['PG', 'CM']}, False),
    ({'floor': 0, 'contains': ['PM', 'CM', 'UM']}, False),
])
def test_day_11_elevator(elevator, valid):
    assert day11.valid_elevator(elevator) == valid

@pytest.mark.parametrize('floors,elevator,valid', [
    ([[], [], [], []], {'floor': 0, 'contains': ['RG']}, True),
    ([[], [], [], []], {'floor': 0, 'contains': ['RM']}, True),
    ([['AG'], [], [], []], {'floor': 0, 'contains': ['AM']}, True),
    ([['AG', 'AM'], [], [], []], {'floor': 0, 'contains': ['BG']}, True),
    ([['AG', 'AM'], [], [], []], {'floor': 0, 'contains': ['BM']}, False),
    ([['AG', 'BM'], [], [], []], {'floor': 0, 'contains': ['BG']}, True),
    ([['AG', 'BG'], [], [], []], {'floor': 0, 'contains': ['BM']}, True),
    ([['AG'], [], [], []], {'floor': 0, 'contains': ['BM']}, False),
    ([['BM'], [], [], []], {'floor': 0, 'contains': ['AG', 'AM']}, False),
    ([['BG'], [], [], []], {'floor': 0, 'contains': ['AG', 'AM']}, True),
    ([['AG', 'BG', 'CG'], [], [], []], {'floor': 0, 'contains': ['UM']}, False),
    ([['AG', 'BG', 'CG', 'CM', 'BM'], [], [], []], {'floor': 0, 'contains': ['UM']}, False),
])
def test_day_11_floor(floors, elevator, valid):
    assert day11.valid_floor(floors, elevator) == valid

@pytest.mark.parametrize('floors,done', [
    ([[], [], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], True),
    ([[], [], ['BG'], ['BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], False),
    ([[], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM'], []], False),
    ([['AG'], ['CM'], ['BG'], ['BM', 'CG', 'UG', 'UM', 'AM', 'LG', 'LM']], False),
])
def test_day_11_done(floors, done):
    assert day11.is_done(floors) == done

def test_day_11():
    floors = [
        ['AM', 'BM'],
        ['AG'],
        ['BG'],
        [],
    ]
    assert day11.solve(floors) == 11





