import pytest

from . import day1, day2

@pytest.mark.parametrize('data,answer,flag', [
    (['1721', '979', '366', '299', '675', '1456'], 514579, False),
])
def test_day_1(data, answer, flag):
    assert day1.solve(data, flag) == answer

@pytest.mark.parametrize('data,answer,flag', [
    (['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'], 2, False),
    (['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'], 1, True),
])
def test_day_2(data, answer, flag):
    assert day2.solve(data, flag) == answer
