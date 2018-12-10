#!/usr/bin/env python
"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

--- Part Two ---

On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.

In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:

    Distance to coordinate A: abs(4-1) + abs(3-1) =  5
    Distance to coordinate B: abs(4-1) + abs(3-6) =  6
    Distance to coordinate C: abs(4-8) + abs(3-3) =  4
    Distance to coordinate D: abs(4-3) + abs(3-4) =  2
    Distance to coordinate E: abs(4-5) + abs(3-5) =  3
    Distance to coordinate F: abs(4-8) + abs(3-9) = 10
    Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30

Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

"""
from __future__ import print_function
import collections
import os


def manhatten(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve(data, flag=False):
    # Only need to care about bounding box
    # Any letter that's on the edge is (probably) part of an infinite size area, can discount
    minx = 1000
    maxx = 0
    miny = 1000
    maxy = 0
    for idx, row in enumerate(data):
        x, y = map(int, row.split(', '))
        maxx = max(maxx, x)
        minx = min(minx, x)
        maxy = max(maxy, y)
        miny = min(miny, y)
    # print(f"x {minx} - {maxx} y {miny} - {maxy}")

    # Grid is all the x, y coordinates and the distances to each point (defined by the index)
    grid = collections.defaultdict(lambda: [1000] * len(data))
    for idx, row in enumerate(data):
        x, y = map(int, row.split(', '))
        for xvar in range(minx, maxx + 1):
            for yvar in range(miny, maxy + 1):
                distance = manhatten(x, y, xvar, yvar)
                grid[xvar, yvar][idx] = distance
    # print(grid)

    # Closest points is the size of the area for each point
    close_area_size = [0] * len(data)
    near_area_size = 0
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if not flag:  # Part 1
                closest_dist = min(grid[x, y])
                if grid[x, y].count(closest_dist) > 1:
                    continue
                closest_idx = grid[x, y].index(closest_dist)
                if x == minx or x == maxx or y == miny or y == maxy:
                    # Edge is infinite, can't be biggest
                    close_area_size[closest_idx] -= 100
                else:
                    close_area_size[closest_idx] += 1
            else:  # Part 2
                if sum(grid[x, y]) < 32:  # Change to 10000 for actual
                    near_area_size += 1
    # print(close_area_size)

    # Part 1
    if not flag:
        return max(close_area_size)
    else:  # Part 2
        return near_area_size


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "day6.input")) as f:
        data = f.read().strip().splitlines()
    print("The size of the largest non-infinite area is", solve(data, False))
    print("The size of the area where all locations are nearby is", solve(data, True))
