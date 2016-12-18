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
import functools
import itertools
import heapq
import os

PRIORITY_Q = False

def priority(floors, elevator):
    """Priority for a State."""
    priority = 3 - elevator
    for i, floor in enumerate(floors):
        priority += (3 - i) * len(floor)
    return priority

def valid_state(floors):
    """Check if state is valid."""
    for floor in floors:
        machines = set(x[0] for x in floor if x[1] == 'M')
        generators = set(x[0] for x in floor if x[1] == 'G')
        unshielded_machines = machines - generators
        if generators and unshielded_machines:
            return False
    return True

def is_done(floors, elevator):
    """Check if done."""
    if elevator != 3:
        return False
    if not floors[0] and not floors[1] and not floors[2] and floors[3]:
        return True
    return False

def freeze(floors):
    """Freeze floors so they can be hashed."""
    return tuple(frozenset(f) for f in floors)


class State(object):
    """State for a step moving machines & generators."""

    def __init__(self, floors, elevator, parents=None):
        self.floors = floors
        self.elevator = elevator
        if parents is None:
            self.parents = []
        else:
            self.parents = parents
        self.priority = priority(self.floors, self.elevator)

    def __str__(self):
        return 'State(%s, E%s, %s, %s)' % (self.floors, self.elevator, len(self.parents), self.priority)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        frozen_floors = freeze(self.floors)
        return hash((frozen_floors, self.elevator))

    def next_state(self):
        """Generate a child state from here."""
        # Move 2 items
        for item, item2 in itertools.combinations(self.floors[self.elevator], 2):
            for dx in (1, -1):
                new_elevator = self.elevator + dx
                if new_elevator not in range(4):
                    continue
                # Move item
                new_floors = copy.deepcopy(self.floors)
                new_floors[self.elevator].remove(item)
                new_floors[new_elevator].append(item)
                new_floors[self.elevator].remove(item2)
                new_floors[new_elevator].append(item2)
                if valid_state(new_floors):
                    yield State(new_floors, new_elevator, parents=self.parents + [self])
        # Move item
        for item in self.floors[self.elevator]:
            for dx in (1, -1):
                new_elevator = self.elevator + dx
                if new_elevator not in range(4):
                    continue
                # Move item
                new_floors = copy.deepcopy(self.floors)
                new_floors[self.elevator].remove(item)
                new_floors[new_elevator].append(item)
                if valid_state(new_floors):
                    yield State(new_floors, new_elevator, parents=self.parents + [self])


def solve(data):
    # Search
    starting_state = State(floors=data, elevator=0)

    if PRIORITY_Q:
        print('priority q')
        queue = []
        heapq.heappush(queue, (starting_state.priority, starting_state))
    else:
        print('deque')
        queue = collections.deque()
        queue.append(starting_state)

    ever_seen = set()
    ever_seen.add(starting_state)

    states = 0
    max_depth = 0
    while queue:
        if PRIORITY_Q:
            _, item = heapq.heappop(queue)
        else:
            item = queue.popleft()
        print('popped', item)
        if len(item.parents) > max_depth:
            max_depth = len(item.parents)
            print('max depth', max_depth, 'states', states, 'len q', len(queue))
        if is_done(item.floors, item.elevator):
            print('The number of steps to move everything is', len(item.parents))
            return len(item.parents)
        ever_seen.add(item)
        for new_item in item.next_state():
            if new_item not in ever_seen:
                print('added', new_item)
                if PRIORITY_Q:
                    heapq.heappush(queue, (new_item.priority, new_item))
                else:
                    queue.append(new_item)
        states += 1

    print('fallthrough')
    return None


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day11.input')) as f:
        data = f.read()
    data = [  # Holly
        ['AG', 'AM'],
        ['BG', 'CG', 'DG', 'EG'],
        ['BM', 'CM', 'DM', 'EM'],
        [],
    ]

    solve(data)

