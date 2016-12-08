#!/usr/bin/env python
"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code should is the screen trying to display?

"""
import os

def draw_rect(grid, width, height):
    for x in range(width):
        for y in range(height):
            grid[y][x] = '#'
    return grid

def rotate_col(grid, column, amount):
    column_list = [grid[x][column] for x in range(len(grid))]
    column_list = column_list[-amount:] + column_list[:-amount]  # Rotate
    for new_val, row in zip(column_list, grid):
        row[column] = new_val
    return grid

def rotate_row(grid, row, amount):
    grid[row] = grid[row][-amount:] + grid[row][:-amount]  # Rotate
    return grid

def solve(data, grid_width, grid_height):
    grid = []
    for _ in range(grid_height):
        grid.append(['.'] * grid_width)

    for instruction in data:
        instruction = instruction.split()
        if instruction[0] == 'rect':
            width, height = instruction[1].split('x')
            width = int(width)
            height = int(height)
            grid = draw_rect(grid, width, height)
        elif instruction[0] == 'rotate':
            if instruction[1] == 'row':
                row_id = int(instruction[2].replace('y=', ''))
                amount = int(instruction[4])
                grid = rotate_row(grid, row_id, amount)
            elif instruction[1] == 'column':
                col_id = int(instruction[2].replace('x=', ''))
                amount = int(instruction[4])
                grid = rotate_col(grid, col_id, amount)

    # Print screen
    for row in grid:
        print(''.join(row))

    # Count lit
    lit = 0
    for row in grid:
        lit += sum(1 for x in row if x == '#')
    return lit


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day8.input')) as f:
        data = f.read().splitlines()

    print('The number of lit lights is', solve(data, 50, 6))
