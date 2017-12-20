#!/usr/bin/env python
"""
--- Day 19: A Series of Tubes ---

Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

    Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
    Travel right, up, and right, passing through B in the process.
    Continue down (collecting C), right, and up (collecting D).
    Finally, go all the way left through E and stopping at F.

Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)

--- Part Two ---

The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

    6 steps down (including the first line at the top of the diagram).
    3 steps right.
    4 steps up.
    3 steps right.
    4 steps down.
    3 steps right.
    2 steps up.
    13 steps left (including the F it stops on).

This would result in a total of 38 steps.

How many steps does the packet need to go?

"""
from __future__ import print_function
import os
import string

def move_direction(x, y, direction):
    if direction == 'U':
        y -= 1
    elif direction == 'D':
        y += 1
    elif direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    return x, y

def get_data(data, x, y):
    try:
        return data[y][x]
    except IndexError:
        return ' '

def generate_directions(data, x, y, direction, letters=False):
    if letters:
        addwith = string.ascii_letters
    else:
        addwith = ''
    new_dirs = set()
    if get_data(data, x - 1, y) in '-' + addwith:
        new_dirs.add('L')
    if get_data(data, x + 1, y) in '-' + addwith:
        new_dirs.add('R')
    if get_data(data, x, y + 1) in '|' + addwith:
        new_dirs.add('D')
    if get_data(data, x, y - 1) in '|' + addwith:
        new_dirs.add('U')
    # Don't double back
    if direction == 'U':
        new_dirs -= set('D')
    elif direction == 'D':
        new_dirs -= set('U')
    elif direction == 'R':
        new_dirs -= set('L')
    elif direction == 'L':
        new_dirs -= set('R')
    return new_dirs

def solve(data, flag=False):
    data = data.split('\n')
    x, y = 0, 0
    x = data[0].index('|')
    letters = []
    direction = 'D'
    stepcount = 0

    while data[y][x] != ' ':
        active = get_data(data, x, y)
        if active == '+':
            # Where to go next?
            # Never 2 corners next to each other
            # Don't go back same way
            # Always - | or letter, try the letter second
            new_dirs = generate_directions(data, x, y, direction)
            if len(new_dirs) == 0:
                # print('Check for letters')
                new_dirs = generate_directions(data, x, y, direction, letters=True)

            if len(new_dirs) == 0:
                print('Nowhere to go. Done??')
                break
            if len(new_dirs) > 1:
                print("Too many direction options!")
                break
            direction = new_dirs.pop()
        elif active not in '|-+':
            letters.append(active)

        x, y = move_direction(x, y, direction)
        stepcount += 1
        if stepcount > 5000000:
            print('Too far!')
            break

    if flag:
        return stepcount
    else:
        return ''.join(letters)


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day19.input')) as f:
        data = f.read()
    print('The packet sees', solve(data, False))
    print('The packet takes', solve(data, True), 'steps.')
