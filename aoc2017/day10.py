#!/usr/bin/env python
"""
--- Day 10: Knot Hash ---

You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind the Elves later not to invent their own cryptographic functions.

This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed, the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting hash.

  4--5   pinch   4  5           4   1
 /    \  5,0,1  / \/ \  twist  / \ / \
3      0  -->  3      0  -->  3   X   0
 \    /         \ /\ /         \ / \ /
  2--1           2  1           2   5

To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:

    Reverse the order of that length of elements in the list, starting with the element at the current position.
    Move the current position forward by that length plus the skip size.
    Increase the skip size by one.

The list is circular; if the current position and the length try to reverse elements beyond the end of the list, the operation reverses using as many extra elements as it needs from the front of the list. If the current position moves past the end of the list, it wraps around to the front. Lengths larger than the size of the list are invalid.

Here's an example using a smaller list:

Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.

    The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
    The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
    After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
    Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.

    The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
    The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
    The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it wraps around: 4 3 0 [1] 2. The skip size increases to 2.

    The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
    The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.

    The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
    Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.

In this example, the first two numbers in the list end up being 3 and 4; to check the process, you can multiply them together to produce 12.

However, you should instead use the standard list size of 256 (with values 0 to 255) and the sequence of lengths in your puzzle input. Once this process is complete, what is the result of multiplying the first two numbers in the list?

"""
from __future__ import print_function
import functools
import os

class CircularList(list):
    def __getitem__(self, x):
        if isinstance(x, slice):
            start, stop, step = x.start, x.stop, x.step
            if start is None:
                start = 0
            if stop is None:
                stop = len(self)
            if step is None:
                step = 1
            return [self[x] for x in range(start, stop, step)]
        return super().__getitem__(x % len(self))

    def __setitem__(self, key, value):
        # print('key value', key, value, type(key), type(value))
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            if start is None:
                start = 0
            if stop is None:
                stop = len(self)
            if step is None:
                step = 1
            for idx, val in zip(range(start, stop, step), value):
                self[idx] = val
            return
        return super().__setitem__(key % len(self), value)

def knothashround(lengths, string, position, skip):
    for length in lengths:
        selected = string[position:position + length]
        string[position:position + length] = list(reversed(selected))
        position += length + skip
        position %= len(string)
        skip += 1
    return string, position, skip

def densify(sparse_hash):
    dense_hash = []
    for idx in range(0, 256, 16):
        block = sparse_hash[idx:idx + 16]
        reduced = functools.reduce(lambda x, y: x ^ y, block)
        dense_hash.append(reduced)
    return dense_hash

def hexify(dense_hash):
    strs = list(map(lambda num: f'{num:02x}', dense_hash))
    return ''.join(strs)


def solve(data, size=256, flag=False):
    if flag:
        lengths = list(map(ord, data)) + [17, 31, 73, 47, 23]
    else:
        lengths = list(map(int, data.split(',')))
    string = CircularList(range(size))
    position = 0
    skip = 0

    if not flag:
        string, _, _ = knothashround(lengths, string, position, skip)
        return string[0] * string[1]

    for _ in range(64):
        string, position, skip = knothashround(lengths, string, position, skip)

    dense_hash = densify(string)

    knot_hash = hexify(dense_hash)

    return knot_hash


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day10.input')) as f:
        data = f.read().strip()
    print('The product of the first two numbers is', solve(data, flag=False))
    print('The knot hash is', solve(data, flag=True))
