#!/usr/bin/env python
"""
--- Day 21: Fractal Art ---

You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###

Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

    If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
    Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.

When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.

Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#

As before, the program begins with this pattern:

.#.
..#
###

The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#

The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#

Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...

Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......

Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?


"""
from __future__ import print_function
import os

def tupleify(s):
    return tuple(tuple(x) for x in s.split('/'))

def all_rotations(rule):
    def rot_cw(x):
        return tuple(zip(*reversed(x)))

    # Original
    o = tupleify(rule)
    yield tupleify(rule)
    # Rotate 3 times
    r1 = rot_cw(o)
    yield r1
    r2 = rot_cw(r1)
    yield r2
    yield rot_cw(r2)
    # Flip, rotate 3 times
    flipped = tuple(tuple(reversed(x)) for x in o)
    yield flipped
    rr1 = rot_cw(flipped)
    yield rr1
    rr2 = rot_cw(rr1)
    yield rr2
    yield rot_cw(rr2)

def print_grid(g):
    for row in g:
        print(''.join(str(e) for e in row))

def solve(data, iterations=5, flag=False):
    print('iterations', iterations)
    # Parse instructions
    enhancements = {}
    for row in data.splitlines():
        lhs, rhs = row.split(' => ')
        rhs = tupleify(rhs)
        # Create dict of all permutations of key -> value
        for rule in all_rotations(lhs):
            enhancements[rule] = rhs

    original = tupleify('.#./..#/###')
    print_grid(original)
    # For iterations
    for _ in range(iterations):
        # Divide into 2/3 size squares
        size = len(original[0])
        if size % 2 == 0:
            split = 2
            new_size = size * 3 // 2
        elif size % 3 == 0:
            split = 3
            new_size = size * 4 // 3
        print('split', split, 'sz', new_size)
        # Make new grid to put them in
        new_grid = []
        for _ in range(new_size):
            new_grid.append([None] * new_size)
        # Break into squares
        new_x = new_y = 0
        for x in range(0, size, split):
            for y in range(0, size, split):
                # Get square
                square = tuple(r[x:x+split] for r in original[y:y+split])
                # Apply rule
                new_square = enhancements[square]
                print('ns', new_square)
                # Assign to new_grid
                for dy, row in enumerate(new_square):
                    for dx, elem in enumerate(row):
                        new_grid[x+dx][y+dy] = elem
            #     new_y += split + 1
            # new_y = 0
            # new_x += split + 1

        original = tuple(tuple(x) for x in new_grid)
        print_grid(original)

    # Sum on pixels
    count = 0
    for row in original:
        count += row.count('#')

    return count


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day21.input')) as f:
        data = f.read().strip()
    print(solve(data, False))
    # print(solve(data, True))
