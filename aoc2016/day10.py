#!/usr/bin/env python
"""
--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

--- Part Two ---

What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

"""
import collections
import os


def run_bots(bots, bot_id, outputs, full_bots):
    bot = bots[bot_id]
    if len(bot['values']) == 2:
        # Pass along values
        low, high = sorted(bot['values'])
        high_bot = bot['high']
        low_bot = bot['low']

        # Give high value
        if 'output' not in high_bot:
            high_bot = high_bot.replace('bot', '')
            bots[high_bot]['values'] += [high]
            if len(bots[high_bot]['values']) == 2:
                full_bots.append(high_bot)
        else:
            outputs[high_bot] = high
        # Give low value
        if 'output' not in low_bot:
            low_bot = low_bot.replace('bot', '')
            bots[low_bot]['values'] += [low]
            if len(bots[low_bot]['values']) == 2:
                full_bots.append(low_bot)
        else:
            outputs[low_bot] = low

    return bots, outputs, full_bots


def solve(data, goal1, goal2, output_goal=False):
    comparing_bot = None
    bots = collections.defaultdict(lambda: {'values': []})
    full_bots = []
    outputs = {}
    for row in data:
        row = row.split()
        if row[0] == 'value':
            # Add to list of values
            bot_id = row[5]
            value = row[1]
            bots[bot_id]['values'] += [int(value)]
            if len(bots[bot_id]['values']) == 2:
                full_bots.append(bot_id)
        elif row[0] == 'bot':
            # Add high & low dest
            bots[row[1]].update({'high': row[10] + row[11], 'low': row[5] + row[6]})

    # Run on bots that have both inputs
    for bot_id in full_bots:
        if bots[bot_id]['values'] == [goal1, goal2] or bots[bot_id]['values'] == [goal2, goal1]:
            comparing_bot = bot_id
        bots, outputs, full_bots = run_bots(bots, bot_id, outputs, full_bots)

    if output_goal:
        return outputs['output0'] * outputs['output1'] * outputs['output2']
    else:
        return comparing_bot


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day10.dale.input')) as f:
        data = f.read().splitlines()

    print('The bot that compares 61 and 17 is', solve(data, 61, 17))
    print('The product of outputs 0, 1 & 2 is', solve(data, 61, 17, output_goal=True))
