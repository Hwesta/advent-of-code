#!/usr/bin/env python
"""
--- Day 18: Duet ---

You discover a tablet containing some strange assembly code labeled simply "Duet". Rather than bother the sound card with it, you decide to run the code yourself. Unfortunately, you don't see any documentation, so you're left to figure out what the instructions mean on your own.

It seems like the assembly is meant to operate on a set of registers that are each named with a single letter and that can each hold a single integer. You suppose each register should start with a value of 0.

There aren't that many instructions, so it shouldn't be hard to figure out what they do. Here's what you determine:

    snd X plays a sound with a frequency equal to the value of X.
    set X Y sets register X to the value of Y.
    add X Y increases register X by the value of Y.
    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
    rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
    jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

Many of the instructions can take either a register (a single letter) or a number. The value of a register is the integer it contains; the value of a number is that number.

After each jump instruction, the program continues with the instruction to which the jump jumped. After any other instruction, the program continues with the next instruction. Continuing (or jumping) off either end of the program terminates it.

For example:

set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2

    The first four instructions set a to 1, add 2 to it, square it, and then set it to itself modulo 5, resulting in a value of 4.
    Then, a sound with frequency 4 (the value of a) is played.
    After that, a is set to 0, causing the subsequent rcv and jgz instructions to both be skipped (rcv because a is 0, and jgz because a is not greater than 0).
    Finally, a is set to 1, causing the next jgz instruction to activate, jumping back two instructions to another jump, which jumps again to the rcv, which ultimately triggers the recover operation.

At the time the recover operation is executed, the frequency of the last sound played is 4.

What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?

--- Part Two ---

As you congratulate yourself for a job well done, you notice that the documentation has been on the back of the tablet this entire time. While you actually got most of the instructions correct, there are a few key differences. This assembly code isn't about sound at all - it's meant to be run twice at the same time.

Each running copy of the program has its own set of registers and follows the code independently - in fact, the programs don't even necessarily run at the same speed. To coordinate, they use the send (snd) and receive (rcv) instructions:

    snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
    rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.

Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.

For example:

snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d

Both programs begin by sending three values to the other. Program 0 sends 1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and stores it in a, receives another value (both 2) and stores it in b, and then each receives the program ID of the other program (program 0 receives 1; program 1 receives 0) and stores it in c. Each program now sees a different value in its own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for either of them, and they reach a deadlock. When this happens, both programs terminate.

It should be noted that it would be equally valid for the programs to run at different speeds; for example, program 0 might have sent all three values and then stopped at the first rcv before program 1 executed even its first instruction.

Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?

"""
from __future__ import print_function
import asyncio
import os
from collections import defaultdict

def compute(instructions, registers, pc, input_buffer, output_buffer):
    def get_value(x):
        try:
            return int(x)
        except ValueError:  # Must be a register
            return registers[x]
    # print('input', input_buffer)
    # print('output_buffer', output_buffer)
    while True:
        # print('registers', registers)
        # print('pc', pc, instructions[pc])
        row = instructions[pc].split()
        action = row[0]
        if action == 'set':
            registers[row[1]] = get_value(row[2])
        elif action == 'add':
            registers[row[1]] += get_value(row[2])
        elif action == 'mul':
            registers[row[1]] *= get_value(row[2])
        elif action == 'mod':
            registers[row[1]] %= get_value(row[2])
        elif action == 'jgz':
            if get_value(row[1]) > 0:
                pc += get_value(row[2])
                pc -= 1   # Compensate for adding to it later
        elif action == 'snd':
            output_buffer.append(get_value(row[1]))
        elif action == 'rcv':
            if input_buffer:
                registers[row[1]] = input_buffer.pop(0)
            else:
                # Return state
                return registers, pc, output_buffer

        pc += 1

def solve(data, flag=False):
    instructions = data.splitlines()
    registers = defaultdict(int)
    pc = 0
    input_buffer = []
    output_buffer = []

    if not flag:
        _, _, output_buffer = compute(
            instructions, registers, pc, input_buffer, output_buffer)
        return output_buffer[0]

    # Run until one runs out of input buffer
    # Run the other
    registers['p'] = 0

    registers2 = defaultdict(int)
    registers2['p'] = 1
    pc2 = 0
    output_buffer2 = []

    i = 0
    sentcount = 0
    while True:
        # Run program 1 until it needs input
        registers, pc, output_buffer = compute(
            instructions, registers, pc, output_buffer2, output_buffer)
        if not output_buffer and not output_buffer2:
            break

        # Feed program 2 input from program 1
        # Run until needs input
        registers2, pc2, output_buffer2 = compute(
            instructions, registers2, pc2, output_buffer, output_buffer2)
        sentcount += len(output_buffer2)

        i+=1
        if i % 1000 == 0:
            print(i)

        # Check if we're done
        if not output_buffer and not output_buffer2:
            break

    return sentcount


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day18.input')) as f:
        data = f.read().strip()
    print('The value of the recovered frequency is', solve(data, False))
    print('The second program sends', solve(data, True), 'values.')
