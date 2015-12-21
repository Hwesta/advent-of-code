#!/usr/bin/env python3
"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH

Given the replacements above and starting with HOH, the following molecules could be generated:

    HOOH (via H => HO on the first H).
    HOHO (via H => HO on the second H).
    OHOH (via H => OH on the first H).
    HOOH (via H => OH on the second H).
    HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

"""
import os


def solve(data):
    replacements = []

    for line in data[:-2]:
        line = line.split(' => ')
        replacements.append((line[0], line[1]))

    molecule = data[-1]

    print(molecule)
    print(replacements)
    new_molecules = set()
    for key, value in replacements:
        # Replace each char that matches in molecule, add to set
        if key not in molecule:
            continue
        print(key, molecule.count(key))
        for idx in range(len(molecule)):
            l = len(key)
            if molecule[idx:idx+l] != key:
                continue
            nm = molecule[:idx] + value + molecule[idx+l:]
            new_molecules.add(nm)

    return len(new_molecules)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day19.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('There are', solve(data), 'new molecules from one replacement.')
