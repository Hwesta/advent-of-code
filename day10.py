#!/usr/bin/env python3
# -*- coding: <encoding name> -*-
"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

"""
import itertools


def version1(data):
    new_data = ''
    for key, matches in itertools.groupby(data):
        # This is like 100x slower especially as input increases because it keeps allocating a new string not modifying the one in place and generating page faults
        # new_data = new_data + str(len(list(matches))) + key
        new_data += str(len(list(matches))) + key
    return new_data

def version2(data):
    return ''.join(str(len(list(matches))) + key for key, matches in itertools.groupby(data))


def look_and_say(data, iterations=1, version=version2):
    for _ in range(iterations):
        data = version(data)

    return data

if __name__ == '__main__':
    data = '1113122113'
    print("Look and say after 40 iterations", len(look_and_say(data, 40)))
