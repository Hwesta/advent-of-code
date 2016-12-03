#!/usr/bin/env python
"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

"""
import os


def solve_vertical(data):
    valid_triangles = 0
    count = 0
    set1 = []
    set2 = []
    set3 = []
    for line in data:
        line = [int(x) for x in line.split()]
        count += 1
        set1.append(line[0])
        set2.append(line[1])
        set3.append(line[2])

        if count == 3:
            count = 0
            set1 = sorted(set1)
            set2 = sorted(set2)
            set3 = sorted(set3)
            if set1[0] + set1[1] > set1[2]:
                valid_triangles += 1
            if set2[0] + set2[1] > set2[2]:
                valid_triangles += 1
            if set3[0] + set3[1] > set3[2]:
                valid_triangles += 1
            set1 = []
            set2 = []
            set3 = []

    return valid_triangles

def solve(data):
    valid_triangles = 0

    for line in data:
        a, b, c = sorted(int(x) for x in line.split())
        if a + b > c:
            valid_triangles += 1
    return valid_triangles


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day3.input')) as f:
        data = f.read().splitlines()
    print('The number of valid triangles is', solve(data))
    print('The number of valid vertically aligned triangles is', solve_vertical(data))
