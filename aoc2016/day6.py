#!/usr/bin/env python
"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

"""
from __future__ import print_function

import collections
import os

def solve_better(data, fewest=False):
    # Rotate data
    rotated = zip(*data[::1])
    solution = ''
    for position in rotated:
        histogram = collections.Counter(position).most_common()
        if not fewest:
            solution += histogram[0][0]
        else:
            solution += histogram[-1][0]
    return solution

def solve(data, fewest=False):
    corrected = []
    for i in range(len(data[0])):
        corrected.append({})

    for code in data:
        for i, letter in enumerate(code):
            corrected[i][letter] = corrected[i].get(letter, 0) + 1

    solution = ''
    for pos in corrected:
        histogram = sorted(pos, key=lambda x: pos[x])
        if fewest:
            solution += histogram[0]
        else:
            solution += histogram[-1]
    return solution

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day6.input')) as f:
        data = f.read().split()

    print('The decoded message is', solve(data))
    print('The real decoded message is', solve(data, fewest=True))
