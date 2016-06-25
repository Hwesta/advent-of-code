#!/usr/bin/env python3
"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

    hlf r sets register r to half its current value, then continues with the next instruction.
    tpl r sets register r to triple its current value, then continues with the next instruction.
    inc r increments register r, adding 1 to it, then continues with the next instruction.
    jmp offset is a jump; it continues with the instruction offset away relative to itself.
    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is finished executing?

--- Part Two ---

The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

"""
from __future__ import division
import os

def hlf(param, registers, pc):
    register = param.strip()
    registers[register] /= 2
    return registers, pc + 1

def tpl(param, registers, pc):
    register = param.strip()
    registers[register] *= 3
    return registers, pc + 1

def inc(param, registers, pc):
    register = param.strip()
    registers[register] += 1
    return registers, pc + 1

def jmp(param, registers, pc):
    pc_inc = int(param)
    return registers, pc + pc_inc

def jie(param, registers, pc):
    register, pc_inc = param.split(',')
    if registers[register.strip()] % 2 == 0:
        return jmp(pc_inc, registers, pc)
    return registers, pc + 1

def jio(param, registers, pc):
    register, pc_inc = param.split(',')
    if registers[register.strip()] == 1:
        return jmp(pc_inc, registers, pc)
    return registers, pc + 1

def solve(data, a=0):
    instruction_set = {
        'hlf': hlf,
        'tpl': tpl,
        'inc': inc,
        'jmp': jmp,
        'jie': jie,
        'jio': jio,
    }
    registers = {'a': a, 'b': 0}

    pc = 0
    while True:
        try:
            instruction = data[pc]
        except IndexError:
            break
        action = instruction[:3]
        registers, pc = instruction_set[action](instruction[3:], registers, pc)

    return registers

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day23.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('If a=0, the value in register b is', solve(data)['b'])
    print('If a=1, the value in register b is', solve(data, a=1)['b'])
