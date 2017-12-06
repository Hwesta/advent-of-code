#!/usr/bin/env python
"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

"""
from __future__ import print_function, division
import os

def solve(data, flag=False):
    data = data.splitlines()
    valid_count = 0
    for row in data:
        words = row.split()
        unique = set()
        valid = True
        for word in words:
            if flag:
                anagramify = set()
                for letter in word:
                    anagramify.add((letter, word.count(letter)))
                word = frozenset(anagramify)
            if word not in unique:
                unique.add(word)
            else:
                valid = False
                break
        valid_count += valid
    return valid_count


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day4.input')) as f:
        data = f.read().strip()
    print(solve(data, False), 'passphrases are valid.')
    print(solve(data, True), 'passphrases are valid, disallowing anagrams.')
