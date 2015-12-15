#!/usr/bin/env python3
"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

"""
import collections
from functools import reduce
import os
import operator

def generate_permutations(list_len, total):
    # From http://stackoverflow.com/questions/7748442/generate-all-possible-lists-of-length-n-that-sum-to-s-in-python
    if list_len == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for j in generate_permutations(list_len - 1, total - i):
                yield (i,) + j


def calc_score(ingredients, amounts, max_cal=None):
    attrib_scores = collections.defaultdict(int)
    cal_score = 0
    for ingredient, amount in zip(ingredients, amounts):
        for attrib, value in ingredients[ingredient].items():
            if attrib == 'calories':
                cal_score += amount * value
            else:
                attrib_scores[attrib] += amount * value
    for attrib, score in attrib_scores.items():
        attrib_scores[attrib] = max(score, 0)

    if max_cal and cal_score != max_cal:
        return 0

    return reduce(operator.mul, attrib_scores.values())


def make_best_cookie(data, max_cal=None):
    ingredients = collections.OrderedDict()
    for row in data:
        row = row.replace(',', '').split()
        ingredients[row[0]] = {
            'capacity': int(row[2]),
            'durability': int(row[4]),
            'flavor': int(row[6]),
            'texture': int(row[8]),
            'calories': int(row[10]),
        }

    max_score = 0
    for ordering in generate_permutations(len(ingredients), 100):
        score = calc_score(ingredients, ordering, max_cal)
        max_score = max(score, max_score)

    return max_score

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day15.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('The best cookie has a score of', make_best_cookie(data))
    print('The best cookie for 500 calories has a score of', make_best_cookie(data, max_cal=500))
