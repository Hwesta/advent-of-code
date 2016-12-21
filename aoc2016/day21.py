#!/usr/bin/env python
"""
--- Day 21: Scrambled Letters and Hash ---

The computer system you're breaking into uses a weird scrambling function to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.

The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:

    swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
    swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
    rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
    rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
    move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

For example, suppose you start with abcde and perform the following operations:

    swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
    swap letter d with letter b swaps the positions of d and b: edcba.
    reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
    rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
    move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
    move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
    rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
    rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

--- Part Two ---

You scrambled the password correctly, but you discover that you can't actually modify the password file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.

What is the un-scrambled version of the scrambled password fbgdceah?

"""
from __future__ import print_function

import collections
import os

def swap_pos(password, idx, idy):
    password[idx], password[idy] = password[idy], password[idx]
    return password

def swap_val(password, val1, val2):
    def swap(x):
        if x == val1:
            return val2
        elif x == val2:
            return val1
        else:
            return x
    password = [swap(x) for x in password]
    return password

def rotate(password, dir, amount, unscramble=False):
    if not unscramble and dir == 'left':
        amount *= -1
    if unscramble and dir == 'right':
        amount *= -1
    deq = collections.deque(password)
    deq.rotate(amount)
    return list(deq)

def rotate_val(password, letter, unscramble=False):
    idx = password.index(letter)
    if unscramble:
        rotated_correctly = []
        for i in range(len(password)):
            test_val = rotate(password, 'left', i)
            rotated = rotate_val(test_val, letter)  # Normal op
            if password == rotated:
                rotated_correctly.append(test_val)
        if len(rotated_correctly) == 1:
            return rotated_correctly[0]
        else:  # This is an error but never occurs in my input
            print('ERROR unscramble rotate by value', password)
            return rotated_correctly[0]
    else:
        if idx >= 4:
            idx += 1
        idx += 1
        return rotate(password, 'right', idx)

def reverse_range(password, start, end):
    password = password[:start] + list(reversed(password[start:end + 1])) + password[end + 1:]
    return password

def move(password, move_from, move_to, unscramble=False):
    if unscramble:
        move_from, move_to = move_to, move_from
    val = password.pop(move_from)
    password.insert(move_to, val)
    return password


def solve(data, password='abcdefgh', unscramble=False):
    password = list(password)
    if unscramble:
        data = reversed(data)
    for row in data:
        row = row.split()
        if row[0] == 'swap' and row[1] == 'position':
            password = swap_pos(password, int(row[2]), int(row[-1]))
        elif row[0] == 'swap' and row[1] == 'letter':
            password = swap_val(password, row[2], row[-1])
        elif row[0] == 'rotate' and row[1] in ('right', 'left'):
            password = rotate(password, row[1], int(row[2]), unscramble=unscramble)
        elif row[0] == 'rotate' and row[1] == 'based':
            password = rotate_val(password, row[-1], unscramble=unscramble)
        elif row[0] == 'reverse':
            password = reverse_range(password, int(row[2]), int(row[-1]))
        elif row[0] == 'move':
            password = move(password, int(row[2]), int(row[-1]), unscramble=unscramble)
        else:
            print('ERROR', row)
    return ''.join(password)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day21.input')) as f:
        data = f.read().splitlines()

    print('The scrambled password is', solve(data))
    print('The unscramble password is', solve(data, password='fbgdceah', unscramble=True))
