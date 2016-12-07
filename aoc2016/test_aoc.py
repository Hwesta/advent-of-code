"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3, day4, day5, day6, day7


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
