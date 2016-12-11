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
from __future__ import division
import collections
import copy
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
        self.floors = floors
        self.elevator = elevator
        self.state_history = []
        if parents is None:
            self.parents = []
        else:
            self.parents = parents

    def __eq__(self, other):
        # Return true if they are equivalent - ie type-rotated
        if self.elevator['floor'] != other.elevator['floor']:
            return False
        floor = self.elevator['floor']
        # Naive - needs to check for type rotation
        self_items = set(self.floors[floor] + self.elevator['contains'])
        other_items = set(other.floors[floor] + other.elevator['contains'])
        return self_items == other_items


    def __hash__(self):
        # So can be put in a set
        floors = copy.deepcopy(self.floors)
        floor = self.elevator['floor']
        floors[floor] += self.elevator['contains'] + ['E']
        return tuple(tuple(f) for f in floors)

    def new_state(self):
        """Generate a child state from here."""
        # Options:
        # Bring 1 item up
        # Bring 2 items up
        # Bring 1 item down
        # Bring 2 items down

def valid_elevator(elevator):
    """Check if the elevator has 0-2 items & doesn't fry anything."""
    num_items = len(elevator['contains'])
    if num_items <= 0:  # Empty, can't move
        return False
    elif num_items == 1:  # One item can't conflict
        return True
    elif num_items == 2:  # Two items
        thing = [i[1] for i in elevator['contains']]
        if thing.count('M') == 2 or thing.count('G') == 2:  # Same thing
            return True
        # M & G
        types = [i[0] for i in elevator['contains']]
        if types[0] == types[1]:  # Same type
            return True
        else:  # Mismatched M & G
            return False
    elif num_items > 2:  # Too many items
        return False


def valid_floor(floors, elevator):
    """Nothing is fried on the floor with this elevator."""
    floor = elevator['floor']
    all_things = floors[floor] + elevator['contains']
    all_machines = set(t[0] for t in all_things if t[1] == 'M')
    all_generators = set(t[0] for t in all_things if t[1] == 'G')

    unshielded_machines = all_machines - all_generators

    if not all_generators:
        return True
    if not unshielded_machines:
        return True
    if all_generators and unshielded_machines:
        return False

    # Error
    return None


def is_done(floors):
    """Check if everything is on fourth floor."""
    return len(floors[0]) + len(floors[1]) + len(floors[2]) == 0
    # return set(('AG', 'AM', 'BG', 'BM', 'CG', 'CM', 'DG', 'DM', 'EG', 'EM')) == set(floors[3])




def solve(data):
    floor = data
    elevator = {'floor': 0, 'contains': []}

    queue = collections.deque()
    starting_state =
    queue.append(TinyTree(3))
    ever_seen = set()
    steps = 0
    while queue:
        item = queue.popleft()
        print('popped item', item)
        ever_seen.add(item)
        for new_item in item.next_state():
            print('gen item', new_item)
            if new_item not in ever_seen:  # Check equality??
                print('added')
                queue.append(new_item)
        steps += 1
        print('queue', queue)
        if steps > 7:
            break

    return

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day11.input')) as f:
        data = f.read().splitlines()

    data = [
        ['AG', 'AM'],
        ['BG', 'CG', 'DG', 'EG'],
        ['BM', 'CM', 'DM', 'EM'],
        [],
    ]


    print(solve(data))
