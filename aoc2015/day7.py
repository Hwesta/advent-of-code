#!/usr/bin/env python3
"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describe how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

"""
import re
import os


def AND(x, y):
    return x & y

def OR(x, y):
    return x | y

def LSHIFT(x, y):
    return x << y

def RSHIFT(x, y):
    return x >> y

def NOT(x, _):
    return ~x

def INPUT(x, _):
    return x

def _run_circ(wires, wire):
    """
    Recursively populate the value for `wire` in `wires`
    """
    if isinstance(wires[wire], int):
        return
    if wires[wire]['x'].isdigit():
        x = int(wires[wire]['x'])
    else:  # Is a label; needs eval
        _run_circ(wires, wires[wire]['x'])
        x = wires[wires[wire]['x']]

    if 'y' in wires[wire]:
        if wires[wire]['y'].isdigit():
            y = int(wires[wire]['y'])
        else:  # Is a label; needs eval
            _run_circ(wires, wires[wire]['y'])
            y = wires[wires[wire]['y']]
    else:
        y = None
    wires[wire] = wires[wire]['func'](x, y)

def run_circuit(data):
    wires = {}
    func_dict = {
        'AND': AND,
        'OR': OR,
        'LSHIFT': LSHIFT,
        'RSHIFT': RSHIFT,
        'NOT': NOT,
    }
    # Build circuit
    for i in data:
        in_, wire = i.split(' -> ')
        match = re.match(r'(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+)', in_)
        if match:
            func = match.group(2)
            x = match.group(1)
            y = match.group(3)
            wires[wire] = {'func': func_dict[func], 'x': x, 'y': y}
            continue
        match = re.match(r'NOT (\w+)', in_)
        if match:
            wires[wire] = {'func': NOT, 'x': match.group(1)}
            continue
        # Must be number
        wires[wire] = {'func': INPUT, 'x': in_}

    # Part 2 only
    wires['b'] = 3176
    # Run circuit, recursively
    for wire in wires:
        _run_circ(wires, wire)

    return wires


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day7.input')) as f:
        data = f.read()
    data = data.split('\n')
    print("The output of wire 'a' is", run_circuit(data)['a'])
