#!/usr/bin/env python
"""
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

    Find x*x + 3*x + 2*x*y + y + y*y.
    Add the office designer's favorite number (your puzzle input).
    Find the binary representation of that sum; count the number of bits that are 1.
        If the number of bits that are 1 is even, it's an open space.
        If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

--- Part Two ---

How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?

"""
from __future__ import division, print_function

import heapq
import os

class State(object):
    """State for a step in the maze."""
    GOAL = None
    FAV_NUM = None
    MAX_STEPS = None

    def __init__(self, x, y, parents=None):
        self.x = x
        self.y = y
        if parents is None:
            self.parents = []
        else:
            self.parents = parents
        self.priority = priority(x, y, self.GOAL)

    def __str__(self):
        return 'State: %s, %s' % (self.x, self.y)

    def __repr__(self):
        return 'State(%s, %s)' % (self.x, self.y)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def next_state(self):
        """Generate a child state from here."""
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            x = self.x + move[0]
            y = self.y + move[1]
            if x < 0 or y < 0:
                continue
            if is_open(x, y, self.FAV_NUM):
                if self.MAX_STEPS is None or len(self.parents) < self.MAX_STEPS:
                    yield State(x, y, parents=self.parents + [self])


def priority(x, y, goal):
    """Priority for a State."""
    return abs(goal[0] - x) + abs(goal[1] - y)


def is_open(x, y, fav_num):
    """Is this a wall?"""
    number = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    return bin(number).count('1') % 2 == 0


def solve(fav_num, goal, max_steps=None):
    State.GOAL = goal
    State.FAV_NUM = fav_num
    State.MAX_STEPS = max_steps

    # # Playing
    # grid = []
    # for y in range(7):
    #     row = ['.' if is_open(x,y,fav_num) else '#' for x in range(10)]
    #     grid.append(row)
    # grid[4][7] = 'G'
    # for row in grid:
    #     print(''.join(row))

    # Search
    queue = []
    starting_state = State(1, 1)
    heapq.heappush(queue, (starting_state.priority, starting_state))
    ever_seen = set()
    ever_seen.add(starting_state)
    steps = 0
    max_depth = 0
    while queue:
        priority, item = heapq.heappop(queue)
        if len(item.parents) > max_depth:
            max_depth = len(item.parents)
            # print('max depth', max_depth, 'states', steps, 'len q', len(queue))
        if (item.x, item.y) == goal:
            print('The number of steps to', goal, 'is', len(item.parents))
            return len(item.parents)
        ever_seen.add(item)
        for new_item in item.next_state():
            if new_item not in ever_seen:
                heapq.heappush(queue, (new_item.priority, new_item))
        steps += 1

    print('The number of states we can reach in', max_steps, 'steps is', len(ever_seen))
    return None


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day13.input')) as f:
        data = f.read()
    data = int(data)
    solve(data, goal=(31, 39))
    solve(data, goal=(-1, -1), max_steps=50)
