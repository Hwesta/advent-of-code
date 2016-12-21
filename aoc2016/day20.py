#!/usr/bin/env python
"""
--- Day 20: Firewall Rules ---

You'd like to set up a small hidden computer here so you can use it to get back into the network later. However, the corporate firewall only allows communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?

--- Part Two ---

How many IPs are allowed by the blacklist?

"""
from __future__ import print_function

import os


def solve(data, count=False, max_ip=None):
    bad_ranges = [tuple(map(int, row.split('-'))) for row in data]
    bad_ranges.sort()  # By start, then end
    blacklist_start, blacklist_end = bad_ranges[0]
    valid_ips = 0
    if max_ip:
        bad_ranges.append((max_ip+1, max_ip+1))

    for start, end in bad_ranges[1:]:
        # print('blacklist start, end', blacklist_start, blacklist_end)
        # print('new range', start, end)
        if blacklist_end + 1 >= start:
            blacklist_end = max(blacklist_end, end)
        elif not count:
            # Gap in blacklist - can return lower range max + 1
            return blacklist_end + 1
        else:
            valid_ips += start - blacklist_end - 1
            blacklist_end = max(blacklist_end, end)
            # print('valid ips', valid_ips)

    return valid_ips

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day20.input')) as f:
        data = f.read().splitlines()

    print('The lowest non-blacklisted IP is', solve(data))
    print('The total number of non-blacklisted IP is', solve(data, count=True, max_ip=4294967295))
