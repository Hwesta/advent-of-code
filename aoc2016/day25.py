#!/usr/bin/env python
"""
--- Day 25: Clock Signal ---

You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.

However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

Nothing happens.

You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.

"No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter Bunny installation, and you're definitely not-" You hang up the phone.

You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly compatible with code you worked on just recently.

This antenna code, being a signal generator, uses one extra instruction:

    out x transmits x (either an integer or the value of a register) as the next value for the clock signal.

The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.

What is the lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever?

--- Part Two ---

The antenna is ready. Now, all you need is the fifty stars required to generate the signal for the sleigh, but you don't have enough.

You look toward the sky in desperation... suddenly noticing that a lone star has been installed at the top of the antenna! Only 49 more to go.

"""
from __future__ import print_function

import os


def cpy(params, registers, pc):
    value, dest = params.split()
    if dest not in registers:
        return registers, pc + 1
    try:
        registers[dest] = int(value)
    except Exception:
        registers[dest] = registers[value]
    return registers, pc + 1

def inc(params, registers, pc):
    dest = params.strip()
    if dest not in registers:
        return registers, pc + 1
    registers[dest] += 1
    return registers, pc + 1

def dec(params, registers, pc):
    dest = params.strip()
    if dest not in registers:
        return registers, pc + 1
    registers[dest] -= 1
    return registers, pc + 1

def jnz(params, registers, pc):
    register, distance = params.split()
    try:
        value = int(register)
    except Exception:
        value = registers[register]
    try:
        distance = int(distance)
    except Exception:
        distance = registers[distance]
    if value != 0:
        return registers, pc + distance
    else:
        return registers, pc + 1

def add(params, registers, pc):
    x, y = params.split()
    registers[x] = registers[x] + registers[y]
    registers[y] = 0
    return registers, pc + 3


def solve(data):
    instructions = [[x[:3], x[4:]] for x in data]
    instruction_set = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'add': add,
    }

    a = 0
    while True:
        registers = {'a': a, 'b': 0, 'c': '0', 'd': 0}
        result = run(instructions, registers, instruction_set)
        if result:
            return a
        else:
            a += 1


def run(instructions, registers, instruction_set):
    out = None
    count = 0
    max_count = 10
    pc = 0
    while True:
        try:
            action, params = instructions[pc]
        except IndexError:
            break

        # "add" optimization
        try:
            # inc a
            # dec c
            # jnz c -2
            #  a <- a + c; c<-0
            if (action == 'inc' and
                instructions[pc+1][0] == 'dec' and
                instructions[pc+2][0] == 'jnz'
                ):
                dest = params.strip()
                i1_reg = instructions[pc+1][1][0]
                i2_reg = instructions[pc+2][1][0]
                if i1_reg == i2_reg:
                    action = 'add'
                    params = dest + ' ' + i1_reg
        except IndexError:
            pass

        if action == 'out':
            # print('out', out, registers[params])
            if out != registers[params]:
                count += 1
                out = registers[params]
                pc += 1
            else:
                return None
        else:
            registers, pc = instruction_set[action](params, registers, pc)

        if count > max_count:
            return True

    return 


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day25.input')) as f:
        data = f.read().splitlines()

    print(solve(data), "as 'a' produces a clock signal.")
