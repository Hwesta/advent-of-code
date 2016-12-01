#!/usr/bin/env python3
"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
import os

def move(location, direction):
    if direction == '^':
        return location[0], location[1] + 1
    elif direction == 'v':
        return location[0], location[1] - 1
    elif direction == '>':
        return location[0] + 1, location[1]
    elif direction == '<':
        return location[0] - 1, location[1]


def delivered_houses(data):
    houses = set()
    location = 0, 0
    houses.add(location)
    for d in data:
        location = move(location, d)
        houses.add(location)
    return len(houses)

def delivered_houses_with_robot(data):
    houses = set()
    santa_location = robosanta_location = 0, 0
    houses.add(santa_location)
    houses.add(robosanta_location)
    for idx, d in enumerate(data):
        if idx % 2 == 0:
            santa_location = move(santa_location, d)
            location = santa_location
        else:  # idx %2 == 1
            robosanta_location = move(robosanta_location, d)
            location = robosanta_location
        houses.add(location)
    return len(houses)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day3.input')) as f:
        data = f.read()
    print(delivered_houses(data), "houses receive at least one present.")
    print("With RoboSanta's help,", delivered_houses_with_robot(data), "houses receive at least one present.")
