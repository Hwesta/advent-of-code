#!/usr/bin/env python3
"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

"""
import itertools
import os


def how_many_combinations(data, total=150, find_min=False):
    data = [int(x) for x in data]
    num_combinations = 0
    for n in range(len(data) + 1):
        num_combinations += len(list(x for x in itertools.combinations(data, n) if sum(x) == total))
        if find_min and num_combinations:
            break
    return num_combinations

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day17.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('There are', how_many_combinations(data), 'combinations that will hold 150L of eggnog.')
    print('The minimum number of containers is', how_many_combinations(data, find_min=True))
