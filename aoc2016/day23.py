#!/usr/bin/env python
"""
--- Day 23: Safe Cracking ---

This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who wouldn't hide a star in a safe behind a painting?

The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see 7.

When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your prototype computer! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.

Now, you just need to figure out what output the keypad would have sent to the safe. You extract the assembunny code from the logic chip (your puzzle input).

The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

    For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
    For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
    The arguments of a toggled instruction are not affected.
    If an attempt is made to toggle an instruction outside the program, nothing happens.
    If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
    If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.

For example, given this program:

cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a

    cpy 2 a initializes register a to 2.
    The first tgl a toggles an instruction a (2) away from it, which changes the third tgl a into inc a.
    The second tgl a also modifies an instruction 2 away from it, which changes the cpy 1 a into jnz 1 a.
    The fourth line, which is now inc a, increments a to 3.
    Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions ahead, skipping the dec a instructions.

In this example, the final value in register a is 3.

The rest of the electronics seem to place the keypad entry (the number of eggs, 7) in register a, run the code, and then send the value left in register a to the safe.

What value should be sent to the safe?

--- Part Two ---

The safe doesn't open, but it does make several angry noises to express its frustration.

You're quite sure your logic is working correctly, so the only other thing is... you check the painting again. As it turns out, colored eggs are still eggs. Now you count 12.

As you run the program with this new input, the prototype computer begins to overheat. You wonder what's taking so long, and whether the lack of any instruction more powerful than "add one" has anything to do with it. Don't bunnies usually multiply?

Anyway, what value should actually be sent to the safe?

"""
from __future__ import print_function

import collections
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

def tgl(params, registers, instructions, pc):
    value = params.strip()
    try:
        offset = int(value)
    except Exception:
        offset = registers[value]

    offset += pc

    try:
        mod_action, mod_params = instructions[offset]
    except IndexError:
        mod_action, mod_params = None, None

    if mod_action == 'inc':
        instructions[offset][0] = 'dec'
    elif mod_action in ('dec', 'tgl'):
        instructions[offset][0] = 'inc'
    elif mod_action == 'jnz':
        instructions[offset][0] = 'cpy'
    elif mod_action in ('cpy',):
        instructions[offset][0] = 'jnz'

    return instructions, pc + 1

def add(params, registers, pc):
    x, y = params.split()
    registers[x] = registers[x] + registers[y]
    registers[y] = 0
    return registers, pc + 3


def solve(data, a=7):
    instructions = [[x[:3], x[4:]] for x in data]
    instruction_set = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'tgl': tgl,
        'add': add,
    }
    registers = {'a': a, 'b': 0, 'c': '0', 'd': 0}

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

        if action == 'tgl':
            instructions, pc = tgl(params, registers, instructions, pc)
        else:
            registers, pc = instruction_set[action](params, registers, pc)

    return registers['a']


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day23.input')) as f:
        data = f.read().splitlines()

    print(solve(data))
    print(solve(data, a=12))
