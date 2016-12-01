#!/usr/bin/env python3
"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

"""
import collections
import os
import re

def compare_attr(val1, val2, key, version=1):
    if version == 1:
        return val1 == val2
    # Version 2
    if key in ('cats', 'trees'):
        return val1 > val2
    elif key in ('pomeranians', 'goldfish'):
        return val1 < val2
    else:
        return val1 == val2

def which_sue(data, version=1):
    real_sue_attrs = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    all_sues = collections.defaultdict(None)
    for row in data:
        match = re.match(r'Sue (?P<id>\d+): (?P<key1>\w+): (?P<val1>\d+), (?P<key2>\w+): (?P<val2>\d+), (?P<key3>\w+): (?P<val3>\d+)', row)
        all_sues[match.group('id')] = {
            match.group('key1'): int(match.group('val1')),
            match.group('key2'): int(match.group('val2')),
            match.group('key3'): int(match.group('val3')),
        }

    real_sue = None
    for sue, attrs in all_sues.items():
        if all(compare_attr(value, real_sue_attrs[key], key, version) for key, value in attrs.items()):
            print('Sue', sue, attrs)
            real_sue = sue

    return real_sue

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day16.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('The real Sue is', which_sue(data))
    print('Wait, the real Sue is actually', which_sue(data, version=2))
