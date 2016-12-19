#!/usr/bin/env python
"""
--- Day 19: An Elephant Named Joseph ---

The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy misunderstanding White Elephant parties.

Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

  1
5   2
 4 3

    Elf 1 takes Elf 2's present.
    Elf 2 has no presents and is skipped.
    Elf 3 takes Elf 4's present.
    Elf 4 has no presents and is also skipped.
    Elf 5 takes Elf 1's two presents.
    Niether Elf 1 nor Elf 2 have any presents, so both are skipped.
    Elf 3 takes Elf 5's three presents.

So, with five Elves, the Elf that sits starting in position 3 gets all the presents.

With the number of Elves given in your puzzle input, which Elf gets all the presents?

--- Part Two ---

Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf directly across the circle. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced.

For example, with five Elves (again numbered 1 to 5):

    The Elves sit in a circle; Elf 1 goes first:

      1
    5   2
     4 3

    Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one to the left. Elf 3 leaves the circle, and the rest of the Elves move in:

      1           1
    5   2  -->  5   2
     4 -          4

    Elf 2 steals from the Elf directly across the circle, Elf 5:

      1         1
    -   2  -->     2
      4         4

    Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:

     -          2
        2  -->
     4          4

    Finally, Elf 2 steals from Elf 4:

     2
        -->  2
     -

So, with five Elves, the Elf that sits starting in position 2 gets all the presents.

With the number of Elves given in your puzzle input, which Elf now gets all the presents?

"""
from __future__ import print_function

import os


def solve_across(data):
    elf_count = int(data)
    elves = list(range(elf_count))

    stealing_elf = 0
    while len(elves) > 1:
        stealing_elf_value = elves[stealing_elf]
        steal_from = (stealing_elf + (len(elves) // 2)) % len(elves)
        # print('idx', stealing_elf, 'val', elves[stealing_elf], 'steal from val', elves[steal_from])
        del elves[steal_from]
        stealing_elf = (elves.index(stealing_elf_value) + 1) % len(elves)
        if len(elves) % 1000 == 0:
            print('len elves', len(elves))
        # print(elves)
    print(elves)
    return elves[0] + 1


def solve(data):
    elf_count = int(data)
    elves = [True] * elf_count
    have_presents = elf_count

    stealing_elf = -1
    while have_presents > 1:
        stealing_elf = (stealing_elf + 1) % elf_count
        # print('elf stealing', stealing_elf)
        if elves[stealing_elf]:  # Skip if no presents
            # print('elves', elves)
            steal_from = (stealing_elf + 1) % elf_count
            while True:
                if elves[steal_from]:
                    elves[steal_from] = False
                    have_presents -= 1
                    print(stealing_elf, 'stole from', steal_from)
                    break
                steal_from = (steal_from + 1) % elf_count

    return (stealing_elf + 1 % elf_count)  # 1 indexed


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day19.input')) as f:
        data = f.read()

    # print(solve(data))
    print(solve_across(data))
