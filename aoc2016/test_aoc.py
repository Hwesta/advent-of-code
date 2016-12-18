"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3, day4, day5, day6, day7, day8, day9
from . import day10, day11, day12, day13, day14, day15, day16, day17, day18


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


@pytest.mark.parametrize('floors,valid', [
    ([[], [], [], []], True),
    ([['AM'], [], ['AG'], []], True),
    ([['AG', 'AM'], [], ['BG', 'BM'], []], True),
    ([['AG', 'BG'], ['BM', 'AM'], [], []], True),
    ([['AG', 'AM', 'BG'], [], ['BM'], []], True),
    ([['AG', 'BM'], [], [], ['AM', 'BG']], False),
    ([['AG', 'AM', 'BM'], [], ['BG'], []], False),
    ([['AG', 'BG', 'CG', 'DM'], [], ['DG'], ['AM', 'BM', 'CM']], False),
    ([['AG', 'BG', 'CG', 'BM', 'CM', 'DM'], [], ['DG'], ['AM']], False),
])
def test_day_11_floor(floors, valid):
    assert day11.valid_state(floors) == valid

@pytest.mark.parametrize('floors,elevator,done', [
    ([[], [], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], 3, True),
    ([[], [], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], 2, False),
    ([[], [], ['BG'], ['BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], 3, False),
    ([[], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM'], []], 3, False),
    ([['AG'], ['CM'], ['BG'], ['BM', 'CG', 'UG', 'UM', 'AM', 'LG', 'LM']], 3, False),
])
def test_day_11_done(floors, elevator, done):
    assert day11.is_done(floors, elevator) == done

@pytest.mark.parametrize('s1_floors,s1_elevator,s2_floors,s2_elevator,target', [
    ([[], [], [], []], 0, [[], [], [], []], 0, True),
    ([[], [], [], []], 0, [[], [], [], []], 1, False),
    ([['AG', 'AM'], [], [], []], 0, [['AG', 'AM'], [], [], []], 0, True),
    ([['AM', 'AG'], [], [], []], 0, [['AG', 'AM'], [], [], []], 0, True),
    ([['AG'], ['AM'], [], []], 0, [['AG'], [], ['AM'], []], 0, False),
    ([['AG', 'AM'], [], [], []], 0, [['AG'], [], ['AM'], []], 0, False),
    ([['AG', 'AM'], [], [], []], 0, [[], [], ['AM', 'AG'], []], 0, False),
    ([['LM', 'HM'], ['HG'], ['LG'], []], 0, [['HM', 'LM'], ['HG'], ['LG'], []], 0, True),
    ([['AG', 'AM'], ['BG', 'BM'], [], []], 0, [['BG', 'BM'], ['AG', 'AM'], [], []], 0, True),  # Equiv
    ([['AG', 'AM', 'CG'], ['BG', 'BM'], ['CM'], []], 0, [['BG', 'BM', 'AG'], ['CG', 'CM'], ['AM'], []], 0, True),  # Equiv
])
def test_day_11_state_eq(s1_floors, s1_elevator, s2_floors, s2_elevator, target):
    day11.State.EQUIV_FUNC = True
    s1 = day11.State(s1_floors, s1_elevator)
    s2 = day11.State(s2_floors, s2_elevator)
    visited = set()
    visited.add(s1)
    assert (s2 in visited) == target

@pytest.mark.parametrize('floors,elevator,priority', [
    ([['AG', 'AM'], [], [], []], 0, 9),
    ([['LM', 'HM'], ['HG'], ['LG'], []], 0, 12),
    ([[], [], [], ['BG', 'BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], 3, 0),
    ([[], [], ['BG'], ['BM', 'CG', 'CM', 'UG', 'UM', 'AG', 'AM', 'LG', 'LM']], 2, 2),
])
def test_day_11_priority(floors, elevator, priority):
    assert day11.priority(floors, elevator) == priority

@pytest.mark.parametrize('floors,steps', [
    ([['AG'], [], [], ['AM']], 3),
    ([['AG', 'AM'], [], [], ['BG', 'BM']], 3),
    ([['HM', 'LM'], ['HG'], ['LG'], []], 11),  # Example
    ([['AG', 'AM', 'BG', 'BM'], [], [], []], 15),
])
def test_day_11(floors, steps):
    assert day11.solve(floors) == steps

def test_day_12():
    instruction_set = [
        'cpy 41 a',
        'inc a',
        'inc a',
        'dec a',
        'jnz a 2',
        'dec a',
    ]
    assert day12.solve(instruction_set)['a'] == 42

@pytest.mark.parametrize('x,y,fav_num,open', [
    (0, 0, 10, True),
    (1, 0, 10, False),
    (2, 0, 10, True),
    (3, 0, 10, False),
    (4, 0, 10, False),
    (0, 1, 10, True),
    (0, 2, 10, False),
    (0, 3, 10, False),
    (0, 4, 10, True),
    (6, 5, 10, True),
])
def test_day_13_is_open(x, y, fav_num, open):
    assert day13.is_open(x, y, fav_num) == open

@pytest.mark.parametrize('x,y,goal,priority', [
    (1, 1, (2,2), 2),
    (1, 1, (7,4), 9),
])
def test_day_13_priority(x, y, goal, priority):
    assert day13.priority(x, y, goal) == priority

@pytest.mark.parametrize('x1,y1,x2,y2,target', [
    (1,1, 1,1, True),
    (1,1, 1,2, False)
])
def test_day_13_state_eq(x1, y1, x2, y2, target):
    day13.State.GOAL = 7, 4
    s1 = day13.State(x1, y1)
    s2 = day13.State(x2, y2)
    assert (s1 == s2) == target

@unittest.skip('too slow')
def test_day_13():
    assert day13.solve(10, (7,4)) == 11

def test_day_14():
    assert day14.solve('abc') == 22728

def test_day_15():
    assert day15.solve([
        'Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.',

    ]) == 5

@pytest.mark.parametrize('data,target', [
    ('1', '100'),
    ('0', '001'),
    ('11111', '11111000000'),
    ('111100001010', '1111000010100101011110000'),
])
def test_day_16_dragon_curve(data, target):
    assert day16.dragon_curve(data) == target

@pytest.mark.parametrize('data,target', [
    ('10000011110010000111', '0111110101'),
    ('0111110101', '01100'),
])
def test_day_16_checksum(data, target):
    assert day16.calc_checksum(data) == target

def test_day_16():
    assert day16.solve('10000', 20) == '01100'

@pytest.mark.parametrize('passcode,path,longest', [
    ('ihgpwlah', 'DDRRRD', False),
    ('kglvqrro', 'DDUDRLRRUDRD', False),
    ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR', False),
    ('hijkl', None, False),
    ('ihgpwlah', 370, True),
    ('kglvqrro', 492, True),
    ('ulqzkmiv', 830, True),
])
def test_day_17(passcode, path, longest):
    assert day17.solve(passcode, longest=longest) == path

@pytest.mark.parametrize('startrow,num_row,num_safe', [
    ('..^^.', 3, 6),
    ('.^^.^.^^^^', 10, 38),
])
def test_day_18(startrow, num_row, num_safe):
    assert day18.solve(startrow, num_row) == num_safe
