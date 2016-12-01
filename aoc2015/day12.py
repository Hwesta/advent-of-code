#!/usr/bin/env python3
"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.

"""
import json
import os
import re


def json_sum(data):
    match = re.findall(r'([\d-]+)', data)
    return sum(map(int, match))


def sum_recursive(elem):
    total = 0
    if isinstance(elem, int):
        return elem
    elif isinstance(elem, dict):
        if 'red' in elem.values():
            return 0
        for i in elem.keys():
            total += sum_recursive(i)
        for i in elem.values():
            total += sum_recursive(i)
    elif isinstance(elem, list):
        for i in elem:
            total += sum_recursive(i)
    return total

def json_sum_not_red(data):
    j = json.loads(data)
    return sum_recursive(j)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day12.input'), 'r') as f:
        data = f.read()
    print('Counting all the numbers, the total is', json_sum(data))
    print('Counting everything not red, the total is', json_sum_not_red(data))
