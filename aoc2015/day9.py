#!/usr/bin/env python3
# -*- coding: <encoding name> -*-
"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and and at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

"""
import collections
import itertools
import os


def calculate_length(ordering, distances):
    length = 0
    for city, next_city in zip(ordering, ordering[1:]):
        length += distances[city][next_city]
    return length

def santa_tsp(data, comparison=min):
    distances = collections.defaultdict(dict)
    for i in data:
        cities, distance = i.split(' = ')
        distance = int(distance)
        src, dst = cities.split(' to ')
        distances[src][dst] = distance
        distances[dst][src] = distance

    cities = distances.keys()
    target_length = None
    for ordering in itertools.permutations(cities):
        length = calculate_length(ordering, distances)
        if target_length is None:
            target_length = length
        target_length = comparison(target_length, length)

    return target_length


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day9.input'), 'r') as f:
        data = f.read()
    data = data.split('\n')
    print("Santa's minimum distance is", santa_tsp(data))
    print("Santa's maximum distance is", santa_tsp(data, comparison=max))
