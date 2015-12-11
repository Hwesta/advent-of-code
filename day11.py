#!/usr/bin/env python3
# -*- coding: <encoding name> -*-
"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doens't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two pairs of letters, like aa, bb, or zz.

For example:

    hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    abbcegjk fails the third requirement, because it only has one double letter (bb).
    The next password after abcdefgh is abcdffaa.
    The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

--- Part Two ---

Santa's password expired again. What's the next one?

"""
import re

def is_valid(pw):
    if any(x in pw for x in 'iol'):
        return False
    if re.search(r'(.)\1.*(.)\2', pw):
        for a, b, c in zip(pw, pw[1:], pw[2:]):
            if ord(a) == ord(b) - 1 == ord(c) - 2:
                return True
    return False

def next_pw(data, idx=-1):
    data[idx] = chr(ord(data[idx]) + 1)
    if data[idx] == 'i':  # Optimizations
        data[idx] = 'j'
    elif data[idx] == 'o':
        data[idx] = 'p'
    elif data[idx] == 'l':
        data[idx] = 'm'
    elif data[idx] > 'z':  # Cycle
        data[idx] = 'a'
        next_pw(data, idx - 1)
    return data

def generate_password(data):
    while True:
        data = ''.join(next_pw(list(data)))
        if is_valid(data):
            break
    return data

if __name__ == '__main__':
    data = 'hxbxwxba'
    print("Santa's next password is", generate_password(data))
    print("Santa's next next password is", generate_password('hxbxxyzz'))
