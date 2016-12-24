#!/usr/bin/env python
"""
--- Day 24: Air Duct Spelunking ---

You've finally met your match; the doors that provide access to the roof are locked tight, and all of the controls and related electronics are inaccessible. You simply can't reach them.

The robot that cleans the air ducts, however, can.

It's not a very fast little robot, but you reconfigure it to be able to interface with some of the exposed wires that have been routed through the HVAC system. If you can direct it to each of those locations, you should be able to bypass the security controls.

You extract the duct layout for this area from some blueprints you acquired and create a map with the relevant locations marked (your puzzle input). 0 is your current location, from which the cleaning robot embarks; the other numbers are (in no particular order) the locations the robot needs to visit at least once each. Walls are marked as #, and open passages are marked as .. Numbers behave like open passages.

For example, suppose you have a map like the following:

###########
#0.1.....2#
#.#######.#
#4.......3#
###########

To reach all of the points of interest as quickly as possible, you would have the robot take the following path:

    0 to 4 (2 steps)
    4 to 1 (4 steps; it can't move diagonally)
    1 to 2 (6 steps)
    2 to 3 (2 steps)

Since the robot isn't very fast, you need to find it the shortest route. This path is the fewest steps (in the above example, a total of 14) required to start at 0 and then visit every other location at least once.

Given your actual map, and starting from location 0, what is the fewest number of steps required to visit every non-0 number marked on the map at least once?

--- Part Two ---

Of course, if you leave the cleaning robot somewhere weird, someone is bound to notice.

What is the fewest number of steps required to start at 0, visit every non-0 number marked on the map at least once, and then return to 0?

"""
from __future__ import print_function

import itertools
import heapq
import os


class Step(object):
    """Step in the maze."""
    MAP = None

    def __init__(self, x, y, parents=None):
        self.x = x
        self.y = y
        if parents is None:
            self.parents = []
        else:
            self.parents = parents
        self.priority = priority(x, y, self.GOAL, len(self.parents))

    def __str__(self):
        return 'Step: %s, %s' % (self.x, self.y)

    def __repr__(self):
        return 'Step(%s, %s)' % (self.x, self.y)

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
            if self.MAP[y][x] == '#':
                continue
            yield Step(x, y, parents=self.parents + [self])

def priority(x, y, goal, current_len):
    """Estimated distance to goal assuming no obstacles."""
    goal_x, goal_y = goal
    priority = current_len + abs(goal_x - x) + abs(goal_y - y)
    return priority


def search_map(maze_map, start_location, goal_location):
    Step.MAP = maze_map
    Step.GOAL = goal_location

    # Search
    queue = []
    starting_state = Step(*start_location)
    heapq.heappush(queue, (starting_state.priority, starting_state))
    ever_seen = set()
    ever_seen.add(starting_state)
    steps = 0
    max_depth = 0
    while queue:
        _, item = heapq.heappop(queue)
        if len(item.parents) > max_depth:
            max_depth = len(item.parents)
        if (item.x, item.y) == goal_location:
            return len(item.parents)
        # Check if all nodes have
        for new_item in item.next_state():
            if new_item not in ever_seen:
                heapq.heappush(queue, (new_item.priority, new_item))
                ever_seen.add(item)
            else:
                new_item.priority = priority(new_item.x, new_item.y, goal_location, len(item.parents))
        steps += 1


def calculate_length(ordering, distances):
    # From AoC 2015 day 9
    length = 0
    for city, next_city in zip(ordering, ordering[1:]):
        length += distances[city][next_city]
    return length


def solve(data, cycle=False):
    # Get location of all #s
    targets = {}
    for y, row in enumerate(data):
        for t in range(10):
            if str(t) in row:
                targets[t] = (row.index(str(t)), y)

    # Set up distances mapping
    distances = [[]] * len(targets)
    for src in range(len(targets)):
        distances[src] = [None for _ in range(len(targets))]

    # Run dijkstra on all targets
    for src in range(len(targets)):
        for dst in range(src, len(targets)):
            start = targets[src]
            goal = targets[dst]
            distance = search_map(data, start, goal)
            distances[src][dst] = distance
            distances[dst][src] = distance

    # Get all permutations of distances, use min
    # From AoC 2015 day 9
    shortest_dist = None
    del targets[0]
    for ordering in itertools.permutations(targets):
        ordering = (0,) + ordering
        if cycle:
            ordering = ordering + (0,)
        length = calculate_length(ordering, distances)
        if shortest_dist is None:
            shortest_dist = length
        shortest_dist = min(shortest_dist, length)

    return shortest_dist


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day24.input')) as f:
        data = f.read().splitlines()

    print('The minimum steps to adjust all wires is', solve(data))
    print('The minimum steps to adjust all wires and return home is', solve(data, cycle=True))
