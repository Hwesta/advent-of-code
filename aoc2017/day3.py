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


37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49  50
"""
from __future__ import print_function
import itertools
import os
import math


def solve(data):
    # Each diagonal down-right is next odd number squared
    # eg 1^2, 3^2, 5^2
    target = int(data)
    print('target', target)
    if target == 1:
        return 0

    # Use odd sqrt to get size of array
    # Generate 2d array
    # How generate?
    # If indexed with 1 at 0,0 x + y == distance
    # Sqrt gives edge len
    # also
    # Get edge len

    # Step down-right to the circle that has the target number in it
    edge_len = math.floor(math.sqrt(target))
    if edge_len % 2 == 0:
        edge_len -= 1
    steps = len([x for x in range(edge_len) if x % 2 != 0])
    x = steps
    y = -steps
    iterator = edge_len * edge_len
    print(f'x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')

    if iterator == target:
        return abs(x) + abs(y)
    x += 1
    iterator += 1
    if target <= iterator + edge_len:
        while iterator < target:
            y += 1
            iterator += 1
            print(f'x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')
        print('found it', iterator, x, y)
        return abs(x) + abs(y)
    print('not in right side, try top')
    iterator += edge_len
    y += edge_len
    edge_len += 1  # Going around longer side
    print(f'top right corner: x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')
    if target <= iterator + edge_len:
        while iterator < target:
            x -= 1
            iterator += 1
            print(f'x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')
        print('found it', iterator, x, y)
        return abs(x) + abs(y)
    print('not in top side, try left')
    iterator += edge_len
    x -= edge_len
    if target <= iterator + edge_len:
        while iterator < target:
            y -= 1
            iterator += 1
            print(f'x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')
        print('found it', iterator, x, y)
        return abs(x) + abs(y)
    print('not in top side, try left')
    iterator += edge_len
    y -= edge_len
    if target <= iterator + edge_len:
        while iterator < target:
            x += 1
            iterator += 1
            print(f'x: {x}, y: {y}, edge_len: {edge_len}, iterator: {iterator}')
        print('found it', iterator, x, y)
        return abs(x) + abs(y)
    raise Exception('Should have found it')


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day3.input')) as f:
        data = f.read()
    print('The number of steps to carry the data back is', solve(data))
