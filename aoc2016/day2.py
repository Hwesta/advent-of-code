#!/usr/bin/env python
"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9

Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

    You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
    Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
    Continuing from "9", you move left, up, right, down, and left, ending with 8.
    Finally, you move up four times (stopping at "2"), then down once, ending with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

    You start at "5" and don't move at all (up and left are both edges), ending at 5.
    Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
    Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
    Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

"""
import os

MOVE = {
    '1': {'U': '1', 'D': '4', 'R': '2', 'L': '1'},
    '2': {'U': '2', 'D': '5', 'L': '1', 'R': '3'},
    '3': {'U': '3', 'D': '6', 'R': '3', 'L': '2'},
    '4': {'U': '1', 'D': '7', 'R': '5', 'L': '4'},
    '5': {'U': '2', 'D': '8', 'R': '6', 'L': '4'},
    '6': {'U': '3', 'D': '9', 'R': '6', 'L': '5'},
    '7': {'U': '4', 'D': '7', 'R': '8', 'L': '7'},
    '8': {'U': '5', 'D': '8', 'R': '9', 'L': '7'},
    '9': {'U': '6', 'D': '9', 'R': '9', 'L': '8'},
}

MOVE_BIG = {
    '1': {'U': '1', 'D': '3', 'R': '1', 'L': '1'},
    '2': {'U': '2', 'D': '6', 'R': '3', 'L': '2'},
    '3': {'U': '1', 'D': '7', 'R': '4', 'L': '2'},
    '4': {'U': '4', 'D': '8', 'R': '4', 'L': '3'},
    '5': {'U': '5', 'D': '5', 'R': '6', 'L': '5'},
    '6': {'U': '2', 'D': 'A', 'R': '7', 'L': '5'},
    '7': {'U': '3', 'D': 'B', 'R': '8', 'L': '6'},
    '8': {'U': '4', 'D': 'C', 'R': '9', 'L': '7'},
    '9': {'U': '9', 'D': '9', 'R': '9', 'L': '8'},
    'A': {'U': '6', 'D': 'A', 'R': 'B', 'L': 'A'},
    'B': {'U': '7', 'D': 'D', 'R': 'C', 'L': 'A'},
    'C': {'U': '8', 'D': 'C', 'R': 'C', 'L': 'B'},
    'D': {'U': 'B', 'D': 'D', 'R': 'D', 'L': 'D'},
}

def solve(data, big=False):
    code = ''
    location = '5'
    if big:
        move_matrix = MOVE_BIG
    else:
        move_matrix = MOVE
    for instruction in data:
        for letter in instruction:
            location = move_matrix[location][letter]
        code += location

    return code


MATRIX = [
    '.....',
    '.123.',
    '.456.',
    '.789.',
    '.....',
]

BIG_MATRIX = [
    '.......',
    '...1...',
    '..234..',
    '.56789.',
    '..ABC..',
    '...D...',
    '.......',
]


def solve_better(data, big=False):
    code = ''
    if big:
        x, y = 1, 3
        move_matrix = BIG_MATRIX
    else:
        x, y = 2, 2
        move_matrix = MATRIX

    for instruction in data:
        for letter in instruction:
            dx = dy = 0
            if letter == 'U':
                dy = -1
            elif letter == 'D':
                dy = 1
            elif letter == 'R':
                dx = 1
            elif letter == 'L':
                dx = -1

            if move_matrix[y + dy][x + dx] != '.':
                x += dx
                y += dy

        code += move_matrix[y][x]

    return code


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day2.input')) as f:
        data = f.read().splitlines()
    print('The bathroom code is', solve_better(data))
    print('The real bathroom code is', solve_better(data, big=True))
