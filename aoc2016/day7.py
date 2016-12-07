#!/usr/bin/env python
"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

"""
import re
import os

import regex

def split_ip(ip):
    # Split based on []
    split = re.split(r'\[|\]', ip)
    # Divide into inside & outside []
    outside = split[::2]
    inside = split[1::2]

    return outside, inside

def support_tls(ip):
    outside, inside = split_ip(ip)

    # Don't match 4 in a row, but match abba
    abba_regex = r'(?!(\w)\1\1\1)(\w)(\w)\3\2'
    # Find any abba outside []
    abba_flag = False
    for o in outside:
        match = re.search(abba_regex, o)
        if match:
            abba_flag = True
            break

    # Check for no abba inside []
    inside_flag = False
    for i in inside:
        match = re.search(abba_regex, i)
        if match:
            inside_flag = True
            break

    if abba_flag and not inside_flag:
        return True
    return False

def support_ssl(ip):
    outside, inside = split_ip(ip)

    # Match three where the first and last are the same
    aba_regex = r'(\w)(\w)\1'

    # Find all possible aba matches
    aba_matches = []
    for o in outside:
        # Need to find overlapping matches
        overlapping_matches = regex.findall(aba_regex, o, overlapped=True)
        if overlapping_matches:
            aba_matches += overlapping_matches

    # Look for a bab in each inside segment
    for i in inside:
        # Check each aba match
        for aba in aba_matches:
            bab = aba[1] + aba[0] + aba[1]
            if bab in i:
                return True

    return False

def solve(data, ssl=False):
    if not ssl:
        return sum(support_tls(ip) for ip in data)
    else:
        return sum(support_ssl(ip) for ip in data)


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day7.input')) as f:
        data = f.read().splitlines()

    print(solve(data), 'IPs support TLS')
    print(solve(data, ssl=True), 'IPs support SSL')
