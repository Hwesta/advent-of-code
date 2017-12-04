#!/usr/bin/env python
"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?

"""
from __future__ import print_function
import itertools
import os
import math


def spiral_iterator(size):
    """Iterator to spiral outwards counterclockwise from center of 2d plane."""
    x = y = 0
    yield x, y
    for length in range(1, size, 2):
        x += 1
        yield x, y
        for _ in range(length):
            y -= 1
            yield x, y
        for _ in range(length + 1):
            x -= 1
            yield x, y
        for _ in range(length + 1):
            y += 1
            yield x, y
        for _ in range(length + 1):
            x += 1
            yield x, y

def print_grid(grid, edge):
    half = edge // 2
    for y in range(-half, half + 1):
        for x in range(-half, half + 1):
            print('{: >3d}'.format(grid[x][y]), end='')
        print()
    print()

def solve(data, stress_test=True):
    target = int(data)
    edge_len = math.ceil(math.sqrt(target))
    if edge_len % 2 == 0:
        edge_len += 1
    edge_len += 1
    grid = []
    for x in range(edge_len):
        grid.append([0] * edge_len)
    counter = 0
    grid[0][0] = 1

    for x, y in spiral_iterator(edge_len):
        if stress_test:
            counter = sum(
                grid[x + dx][y + dy]
                for dx, dy
                in itertools.product([0, 1, -1], repeat=2)
            )
        else:
            counter += 1
        grid[x][y] = counter
        # print_grid(grid, edge_len)
        if not stress_test and counter == target:
            return abs(x) + abs(y)
        if stress_test and counter > target:
            return counter

    raise Exception('Not found')


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day3.input')) as f:
        data = f.read()
    print('The number of steps to carry the data back is', solve(data))
    print('The next largest value in the stress test is', solve(data, True))
