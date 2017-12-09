#!/usr/bin/env python
"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

"""
from __future__ import print_function
import os
import collections
import operator

def solve(data, flag=False):
    registers = collections.defaultdict(int)
    signs = {
        '<': operator.lt,
        '>': operator.gt,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '<=': operator.le,
    }
    actions = {
        'inc': operator.add,
        'dec': operator.sub,
    }
    max_ever = 0

    for row in data.splitlines():
        row = row.split()
        register = row[0]
        action = row[1]
        action_amount = int(row[2])
        condition_register = row[4]
        condition_sign = row[5]
        condition_val = int(row[6])

        if signs[condition_sign](registers[condition_register], condition_val):
            registers[register] = actions[action](registers[register], action_amount)

        curr_max = max(registers.values())
        if curr_max > max_ever:
            max_ever = curr_max
    if flag:
        return max_ever
    else:
        return max(registers.values())


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day8.input')) as f:
        data = f.read().strip()
    print('The largest input in any register is', solve(data, False))
    print('The highest value ever held is', solve(data, True))
