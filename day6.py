#!/usr/bin/env python3
"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""
import ast
import os
import re

def turn_on(state):
    return 1

def turn_off(state):
    return 0

def toggle(state):
    return not state

def winning_lights(data):
    lights = {(x, y): False for x in range(1000) for y in range(1000)}
    for idx, i in enumerate(data):

        if i.startswith('turn on'):
            fn = turn_on
            i = i.replace('turn on ', '')
        elif i.startswith('turn off'):
            fn = turn_off
            i = i.replace('turn off ', '')
        elif i.startswith('toggle'):
            fn = toggle
            i = i.replace('toggle ', '')
        top_left, bottom_right = i.split(' through ')
        top_left = ast.literal_eval(top_left)
        bottom_right = ast.literal_eval(bottom_right)
        min_x = top_left[0]
        min_y = top_left[1]
        max_x = bottom_right[0]
        max_y = bottom_right[1]
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                lights[x, y] = fn(lights[x, y])

    return sum(lights.values())


def turn_on_brightness(state):
    return state + 1

def turn_off_brightness(state):
    return state - 1 if state > 0 else 0

def toggle_brightness(state):
    return state + 2

def winning_lights_brightness(data):
    # Revised iteration through lights, could be the same
    lights = {(x, y): 0 for x in range(1000) for y in range(1000)}
    fn_dict = {
        'turn on ': turn_on_brightness,
        'turn off ': turn_off_brightness,
        'toggle ': toggle_brightness,
    }
    for idx, i in enumerate(data):
        regex = r'(?P<fn>\D+)(?P<min_x>\d+),(?P<min_y>\d+) through (?P<max_x>\d+),(?P<max_y>\d+)'
        match = re.match(regex, i)
        fn = fn_dict[match.group('fn')]
        min_x = int(match.group('min_x'))
        min_y = int(match.group('min_y'))
        max_x = int(match.group('max_x'))
        max_y = int(match.group('max_y'))
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                lights[x, y] = fn(lights[x, y])

    return sum(lights.values())


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day6.input')) as f:
        data = f.read()
    data = data.split('\n')
    print(winning_lights(data), 'lights are lit.')
    print('Total light brightness is', winning_lights_brightness(data))
