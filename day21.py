#!/usr/bin/env python3
"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

    The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

--- Part Two ---

Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

"""
import copy
import collections
import itertools
import os
import operator

WEAPONS = collections.OrderedDict([
    ('Dagger', {'cost':  8, 'damage': 4, 'armor': 0}),
    ('Shortsword', {'cost': 10, 'damage': 5, 'armor': 0}),
    ('Warhammer', {'cost': 25, 'damage': 6, 'armor': 0}),
    ('Longsword', {'cost': 40, 'damage': 7, 'armor': 0}),
    ('Greataxe', {'cost': 74, 'damage': 8, 'armor': 0}),
])
ARMOR = collections.OrderedDict([
    ('Leather', {'cost': 13, 'damage': 0, 'armor': 1}),
    ('Chainmail', {'cost': 31, 'damage': 0, 'armor': 2}),
    ('Splintmail', {'cost': 53, 'damage': 0, 'armor': 3}),
    ('Bandedmail', {'cost': 75, 'damage': 0, 'armor': 4}),
    ('Platemail', {'cost': 102, 'damage': 0, 'armor': 5}),
])
RINGS = collections.OrderedDict([
    ('Damage +1', {'cost': 25, 'damage': 1, 'armor': 0}),
    ('Damage +2', {'cost': 50, 'damage': 2, 'armor': 0}),
    ('Damage +3', {'cost': 100, 'damage': 3, 'armor': 0}),
    ('Defense +1', {'cost': 20, 'damage': 0, 'armor': 1}),
    ('Defense +2', {'cost': 40, 'damage': 0, 'armor': 2}),
    ('Defense +3', {'cost': 80, 'damage': 0, 'armor': 3}),
])

ALL = collections.OrderedDict([
    ('Dagger', {'cost':  8, 'damage': 4, 'armor': 0}),
    ('Shortsword', {'cost': 10, 'damage': 5, 'armor': 0}),
    ('Warhammer', {'cost': 25, 'damage': 6, 'armor': 0}),
    ('Longsword', {'cost': 40, 'damage': 7, 'armor': 0}),
    ('Greataxe', {'cost': 74, 'damage': 8, 'armor': 0}),
    ('Leather', {'cost': 13, 'damage': 0, 'armor': 1}),
    ('Chainmail', {'cost': 31, 'damage': 0, 'armor': 2}),
    ('Splintmail', {'cost': 53, 'damage': 0, 'armor': 3}),
    ('Bandedmail', {'cost': 75, 'damage': 0, 'armor': 4}),
    ('Platemail', {'cost': 102, 'damage': 0, 'armor': 5}),
    ('Damage +1', {'cost': 25, 'damage': 1, 'armor': 0}),
    ('Damage +2', {'cost': 50, 'damage': 2, 'armor': 0}),
    ('Damage +3', {'cost': 100, 'damage': 3, 'armor': 0}),
    ('Defense +1', {'cost': 20, 'damage': 0, 'armor': 1}),
    ('Defense +2', {'cost': 40, 'damage': 0, 'armor': 2}),
    ('Defense +3', {'cost': 80, 'damage': 0, 'armor': 3}),
])
ALL = collections.OrderedDict(sorted(ALL.items(), key=lambda x: x[1]['cost']))

def run_game(boss, player):
    attacker = player
    defender = boss

    while boss['hp'] > 0 and player['hp'] > 0:
        defender['hp'] -= max(1, attacker['damage'] - defender['armor'])
        attacker, defender = defender, attacker

    if player['hp'] > 0:
        return 'player'
    else:
        return 'boss'

def solve(data, cheating_shopkeeper=False):
    boss = {
        'hp': int(data[0].split()[-1]),
        'damage': int(data[1].split()[-1]),
        'armor': int(data[2].split()[-1]),
    }

    winner = 'boss'
    best_cost = 100  # 276 too high
    for n in range(1, 5):
        for itemset in itertools.permutations(ALL, n):
            # Validate legal
            if len([x for x in itemset if x in WEAPONS]) != 1:
                continue
            if len([x for x in itemset if x in ARMOR]) > 1:
                continue
            if len([x for x in itemset if x in RINGS]) > 2:
                continue

            # Run game
            player = {
                'hp': 100,
                'damage': sum(ALL[x]['damage'] for x in itemset),
                'armor': sum(ALL[x]['armor'] for x in itemset)
            }
            winner = run_game(copy.copy(boss), player)
            cost = sum(ALL[x]['cost'] for x in itemset)
            if not cheating_shopkeeper and winner == 'player':
                best_cost = min(best_cost, cost)
            elif cheating_shopkeeper and winner == 'boss':
                best_cost = max(best_cost, cost)
    return best_cost

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day21.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('Minimum gold to beat boss is', solve(data))
    print('Maximum gold to lose to boss is', solve(data, cheating_shopkeeper=True))
