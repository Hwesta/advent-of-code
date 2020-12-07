import pytest

from . import day1

@pytest.mark.parametrize('data,answer,flag', [
    (['1721', '979', '366', '299', '675', '1456'], 514579, False),
])
def test_day_1(data, answer, flag):
    assert day1.solve(data, flag) == answer
