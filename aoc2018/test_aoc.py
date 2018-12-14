"""
Tests for Advent of Code
"""
import unittest

import pytest

from . import day1, day2, day3, day4, day5, day6, day7, day8


@pytest.mark.parametrize(
    "data,answer,flag",
    [
        (["+1", "+1", "+1"], 3, False),
        (["0", "+1"], 1, False),
        (["-1", "+3"], 2, False),
        (["+1", "-1"], 0, True),
        (["+3", "+3", "+4", "-2", "-4"], 10, True),
        (["-6", "+3", "+8", "+5", "-6"], 5, True),
        (["+7", "+7", "-2", "-7", "-4"], 14, True),
    ],
)
def test_day_1(data, answer, flag):
    assert day1.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    (["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"], 12, False),
    (["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"], "fgij", True)
])
def test_day_2(data, answer, flag):
    assert day2.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    (["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 4, False),
    (["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 3, True),
])
def test_day_3(data, answer, flag):
    assert day3.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-02 00:40] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-02 00:50] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-01 00:55] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-05 00:45] falls asleep
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:55] wakes up""".splitlines(), 240, False),
    ("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-02 00:40] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-02 00:50] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-01 00:55] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-05 00:45] falls asleep
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:55] wakes up""".splitlines(), 4455, True),])
def test_day_4(data, answer, flag):
    assert day4.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ("dabAcCaCBAcCcaDA", 10, False),
    ("dabAcCaCBAcCcaDA", 4, True),
])
def test_day_5(data, answer, flag):
    assert day5.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    (["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"], 17, False),
    (["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"], 16, True),
])
def test_day_6(data, answer, flag):
    assert day6.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ([
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ], "CABDFE", False),
    ([
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ], 15, True),
])
def test_day_7(data, answer, flag):
    assert day7.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", 138, False),
])
def test_day_8(data, answer, flag):
    assert day8.solve(data, flag) == answer
