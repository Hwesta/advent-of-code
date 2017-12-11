#!/usr/bin/env python
"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

"""
from __future__ import print_function
import os

def cube_distance(x, y, z):
    return (abs(x) + abs(y) + abs(z)) // 2

def solve(data, flag=False):
    max_distance = 0
    steps = data.split(',')
    x = y = z = 0

    for step in steps:
        if step == 'n':
            y += 1
            z -= 1
        elif step == 'ne':
            x += 1
            z -= 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 's':
            y -= 1
            z += 1
        elif step == 'sw':
            x -= 1
            z += 1
        elif step == 'nw':
            x -= 1
            y += 1
        max_distance = max(max_distance, cube_distance(x, y, z))

    if flag:
        return max_distance
    else:
        return cube_distance(x, y, z)


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day11.input')) as f:
        data = f.read().strip()
    print('The child process is', solve(data, False), 'steps away.')
    print('The furthest the child process wandered was', solve(data, True), 'steps away.')
