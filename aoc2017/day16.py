#!/usr/bin/env python
"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

    Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
    Exchange, written xA/B, makes the programs at positions A and B swap places.
    Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do the following dance:

    s1, a spin of size 1: eabcd.
    x3/4, swapping the last two programs: eabdc.
    pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?


"""
from __future__ import print_function
import os
import string


def spin(dancers, n):
    return dancers[-n:] + dancers[:-n]

def exchange(dancers, x, y):
    dancers[x], dancers[y] = dancers[y], dancers[x]
    return dancers

def partner(dancers, a, b):
    a_idx = dancers.index(a)
    b_idx = dancers.index(b)
    dancers[a_idx] = b
    dancers[b_idx] = a
    return dancers


def solve(data, num_programs=15, flag=False):
    dancers = list(string.ascii_lowercase[:num_programs])
    data = data.split(',')
    for row in data:
        action = row[0]
        if action == 's':
            size = int(row[1:])
            dancers = spin(dancers, size)
        elif action == 'x':
            x, y = row[1:].split('/')
            x, y = int(x), int(y)
            dancers = exchange(dancers, x, y)
        elif action == 'p':
            a, b = row[1:].split('/')
            dancers = partner(dancers, a, b)

    return ''.join(dancers)


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day16.input')) as f:
        data = f.read().strip()
    print(solve(data, 16, flag=False))
    # print(solve(data, 16, flag=True))
