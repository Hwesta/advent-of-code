#!/usr/bin/env python
"""
--- Day 11: Radioisotope Thermoelectric Generators ---

You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby. There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to experiment with Radioisotope Thermoelectric Generators (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to generate an elecromagnetic radiation shield when powered. Unfortunately, they can only be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)

You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the first floor.

For example, suppose the isolated area has the following arrangement:

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.

As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for Lithium, M for Microchip, and G for Generator), the initial state looks like this:

F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM

Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

    Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:

    F4 .  .  .  .  .
    F3 .  .  .  LG .
    F2 E  HG HM .  .
    F1 .  .  .  .  LM

    Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:

    F4 .  .  .  .  .
    F3 E  HG HM LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  LM

    Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 E  .  HM .  .
    F1 .  .  .  .  LM

    At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 .  .  .  .  .
    F1 E  .  HM .  LM

    Bring both Microchips up one floor, where there is nothing to fry them:

    F4 .  .  .  .  .
    F3 .  HG .  LG .
    F2 E  .  HM .  LM
    F1 .  .  .  .  .

    Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:

    F4 .  .  .  .  .
    F3 E  HG HM LG LM
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Microchips to the fourth floor:

    F4 E  .  HM .  LM
    F3 .  HG .  LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

    F4 .  .  .  .  LM
    F3 E  HG HM LG .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:

    F4 E  HG .  LG LM
    F3 .  .  HM .  .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring the Lithium Microchip with you to the third floor so you can use the elevator:

    F4 .  HG .  LG .
    F3 E  .  HM .  LM
    F2 .  .  .  .  .
    F1 .  .  .  .  .

    Bring both Microchips to the fourth floor:

    F4 E  HG HM LG LM
    F3 .  .  .  .  .
    F2 .  .  .  .  .
    F1 .  .  .  .  .

In this arrangement, it takes 11 steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

In your situation, what is the minimum number of steps required to bring all of the objects to the fourth floor?


"""
from __future__ import division, print_function
import collections
import copy
import itertools
import heapq
import os


class TinyTree(object):

    def __init__(self, value, parents=None):
        self.value = value
        if parents is None:
            self.parents = []
        else:
            self.parents = parents

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return 'TinyTree %s' % self.value

    def __repr__(self):
        return 'TinyTree(%s, %s)' % (self.value, [str(s) for s in self.parents])

    def __hash__(self):
        return self.value

    def next_state(self):
        parents = self.parents + [self]
        yield TinyTree(self.value // 2, parents=parents)
        yield TinyTree(max((self.value * 2) - 1, 0), parents=parents)


class State(object):

    def __init__(self, floors, elevator, parents=None):
        self.floors = [sorted(f) for f in floors]
        # Ensure sorted
        self.elevator = elevator
        if parents is None:
            self.parents = []
        else:
            self.parents = parents
        self.priority = priority(floors)

    def __str__(self):
        return 'State: E%s F0: %s; F1: %s; F2: %s; F3: %s' % (
            self.elevator,
            ' '.join(self.floors[0]),
            ' '.join(self.floors[1]),
            ' '.join(self.floors[2]),
            ' '.join(self.floors[3]),
        )

    def __repr__(self):
        return 'State(%s, %s)' % (self.floors, self.elevator)

    def __eq__(self, other):
        # Return true if they are equivalent - ie type-rotated
        if self.elevator != other.elevator:
            return False

        return hash(self) == hash(other)

    def __hash__(self):
        # So can be put in a set
        return hash(normalize_rep(self.floors, self.elevator))

    def next_state(self):
        """Generate a child state from here."""

        # Check if below floors are empty
        empty_below = not sum(len(f) for f in self.floors[:self.elevator])

        brought_2_up = False
        brought_1_down = False

        # Bring 2 items up
        for i1, i2 in itertools.combinations(self.floors[self.elevator], 2):
            # Up
            next_floor = self.elevator + 1
            if next_floor < 4:
                new_floors = copy.deepcopy(self.floors)
                new_floors[self.elevator].remove(i1)
                new_floors[self.elevator].remove(i2)
                new_floors[next_floor].append(i1)
                new_floors[next_floor].append(i2)
                if valid_floor(new_floors):
                    brought_2_up = True
                    yield State(new_floors, next_floor, parents=self.parents + [self])

            if empty_below:
                continue

            # Down
            next_floor = self.elevator - 1
            if next_floor >= 0:
                new_floors = copy.deepcopy(self.floors)
                new_floors[self.elevator].remove(i1)
                new_floors[self.elevator].remove(i2)
                new_floors[next_floor].append(i1)
                new_floors[next_floor].append(i2)
                if valid_floor(new_floors):
                    yield State(new_floors, next_floor, parents=self.parents + [self])

        # Bring 1 item up or down
        for item in self.floors[self.elevator]:
            # Up
            if not brought_2_up:
                next_floor = self.elevator + 1
                if next_floor < 4:
                    new_floors = copy.deepcopy(self.floors)
                    new_floors[self.elevator].remove(item)
                    new_floors[next_floor].append(item)
                    if valid_floor(new_floors):
                        yield State(new_floors, next_floor, parents=self.parents + [self])

            # Down
            if empty_below:
                continue

            next_floor = self.elevator - 1
            if next_floor >= 0:
                new_floors = copy.deepcopy(self.floors)
                new_floors[self.elevator].remove(item)
                new_floors[next_floor].append(item)
                if valid_floor(new_floors):
                    yield State(new_floors, next_floor, parents=self.parents + [self])


def normalize_rep(floors, elevator):
    # Normalize representation - convert
    # [['BM', 'BG', 'CG'], ['CM'], ['AM', 'AG'], []]
    # to
    # [['AM', 'AG', 'BG'], ['BM'], ['CM', 'CG'], []]

    pairs = set()
    floors = copy.deepcopy(floors)
    # Generate pairs
    for i, floor in enumerate(floors):
        for item in floor:
            if item[1] == 'M':
                match = item[0] + "G"
                for j, search_floor in enumerate(floors):
                    if match in search_floor:
                        pairs.add((i, j))
    return (frozenset(pairs), elevator)

def valid_floor(floors):
    for floor in floors:
        """Nothing is fried on the floor with this elevator."""
        all_machines = set(t[0] for t in floor if t[1] == 'M')
        all_generators = set(t[0] for t in floor if t[1] == 'G')

        unshielded_machines = all_machines - all_generators

        if all_generators and unshielded_machines:
            return False

    # Nothing in valid - all are valid
    return True


def is_done(floors):
    """Check if everything is on fourth floor."""
    return len(floors[0]) + len(floors[1]) + len(floors[2]) == 0


def priority(floors):
    priority = 0
    for i, floor in enumerate(floors):
        priority += (3 - i) * len(floor)
    return priority


def solve(data):
    floors = data

    queue = collections.deque()
    queue = []
    starting_state = State(floors, 0)
    heapq.heappush(queue, (starting_state.priority, starting_state))
    ever_seen = set()
    ever_seen.add(starting_state)
    steps = 0
    max_depth = 0
    while queue:
        priority, item = heapq.heappop(queue)
        if len(item.parents) > max_depth:
            max_depth = len(item.parents)
            print('max depth', max_depth, 'states', steps, 'len q', len(queue))
        # print('popped item', item, len(item.parents))
        if is_done(item.floors):
            print('FOUND VALID SOLUTION', len(item.parents), steps)
            return len(item.parents)
        ever_seen.add(item)
        for new_item in item.next_state():
            if new_item not in ever_seen:
                # print('gen item', new_item)
                # print('ever seen', ever_seen)
                # print('added')
                heapq.heappush(queue, (new_item.priority, new_item))
        steps += 1
    print('fallthrough', steps)
    return None

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day11.input')) as f:
        data = f.read().splitlines()

    # Fails
    data = [  # Holly
        ['AG', 'AM'],
        ['BG', 'CG', 'DG', 'EG'],
        ['BM', 'CM', 'DM', 'EM'],
        [],
    ]
    data = [
        ['AG', 'AM', 'BG', 'CG'],
        ['BM', 'CM'],
        ['DG', 'DM', 'EG', 'EM'],
        [],
    ]  # 31

    # Works
    data = [
        ['AG', 'BG', 'BM', 'CG', 'DG', 'DM', 'EG', 'EM'],
        ['AM', 'CM'],
        [],
        [],
    ]  # 47
    data = [
        ['AM', 'AG', 'BM', 'BG'],
        ['CM', 'CG', 'DM', 'DG', 'EG'],
        ['EM'],
        [],
    ]  # 37

    print(solve(data))
