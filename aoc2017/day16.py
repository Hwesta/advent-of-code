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

--- Part Two ---

Now that you're starting to get a feel for the dance moves, you turn your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs perform it again and again: including the first dance, a total of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, and use the same dance moves:

    s1, a spin of size 1: cbaed.
    x3/4, swapping the last two programs: cbade.
    pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?

"""
from __future__ import print_function
import os
import string
import functools

@functools.lru_cache()
def dance(dancers, data):
    # Make mutable
    dancers = list(dancers)
    for row in data:
        action = row[0]
        if action == 's':
            size = int(row[1:])
            dancers = dancers[-size:] + dancers[:-size]
        elif action == 'x':
            x, y = row[1:].split('/')
            x, y = int(x), int(y)
            dancers[x], dancers[y] = dancers[y], dancers[x]
        elif action == 'p':
            a, b = row[1:].split('/')
            a_idx = dancers.index(a)
            b_idx = dancers.index(b)
            dancers[a_idx] = b
            dancers[b_idx] = a
    # Make static
    return tuple(dancers)

def solve(data, num_programs=16, flag=False):
    dancers = tuple(string.ascii_lowercase[:num_programs])
    data = tuple(data.split(','))

    dancers = dance(dancers, data)

    if not flag:
        return ''.join(dancers)

    # Tried running everything: way too slow
    # Tried memoizing input parsing & type conversions: still way too slow
    # Tried mapping input index to output index: doesn't work
    # Tried using functools.lru_cache() faster, but still slow
    # Realized there's only 30 items in lru_cache
    # Tried dictionary lookups: faster!

    memoize = {}
    iterations = 1000000000
    for i in range(iterations - 1):
        if dancers in memoize:
            dancers = memoize[dancers]
            continue
        key = dancers
        dancers = dance(dancers, data)
        value = dancers
        memoize[key] = value

    return ''.join(dancers)


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day16.input')) as f:
        data = f.read().strip()
    print(solve(data, 16, flag=False))
    print(solve(data, 16, flag=True))
