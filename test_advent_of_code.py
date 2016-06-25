"""
Tests for Advent of Code
"""
import collections

import day1, day2, day3, day4, day5, day6, day7, day8, day9
import day10, day11, day12, day13, day14, day15, day17, day18, day19
import day20, day21, day23

def test_day_1():
    version = day1.find_santas_floor_v3
    assert day1.find_santas_floor('(())', version=version) == 0
    assert day1.find_santas_floor('()()', version=version) == 0
    assert day1.find_santas_floor('(((', version=version) == 3
    assert day1.find_santas_floor('(()(()(', version=version) == 3
    assert day1.find_santas_floor('))(((((', version=version) == 3
    assert day1.find_santas_floor('())', version=version) == -1
    assert day1.find_santas_floor('))(', version=version) == -1
    assert day1.find_santas_floor(')))', version=version) == -3
    assert day1.find_santas_floor(')())())', version=version) == -3

    assert day1.basement_entrance(')') == 1
    assert day1.basement_entrance('()())') == 5

def test_day_2():
    assert day2.order_paper(['2x3x4']) == 58
    assert day2.order_paper(['1x1x10']) == 43
    assert day2.order_paper(['2x3x4', '1x1x10']) == 58 + 43

    assert day2.order_ribbons(['2x3x4']) == 34
    assert day2.order_ribbons(['1x1x10']) == 14
    assert day2.order_ribbons(['2x3x4', '1x1x10']) == 34 + 14

def test_day_3():
    assert day3.delivered_houses('>') == 2
    assert day3.delivered_houses('^>v<') == 4
    assert day3.delivered_houses('^v^v^v^v^v') == 2

    assert day3.delivered_houses_with_robot('^v') == 3
    assert day3.delivered_houses_with_robot('^>v<') == 3
    assert day3.delivered_houses_with_robot('^v^v^v^v^v') == 11

def test_day_4():
    assert day4.generate_advent_coins('abcdef') == 609043
    assert day4.generate_advent_coins('pqrstuv') == 1048970

def test_day_5():
    assert day5.nice_strings(['ugknbfddgicrmopn']) == 1
    assert day5.nice_strings(['aaa']) == 1
    assert day5.nice_strings(['jchzalrnumimnmhp']) == 0
    assert day5.nice_strings(['haegwjzuvuyypxyu']) == 0
    assert day5.nice_strings(['dvszwmarrgswjxmb']) == 0

    assert day5.better_nice_strings(['qjhvhtzxzqqjkmpb']) == 1
    assert day5.better_nice_strings(['xxyxx']) == 1
    assert day5.better_nice_strings(['uurcxstgmygtbstg']) == 0
    assert day5.better_nice_strings(['ieodomkazucvgmuy']) == 0

def test_day_6():
    assert day6.winning_lights(['turn on 0,0 through 999,999']) == 1000000
    assert day6.winning_lights(['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0']) == 1000000 - 1000
    assert day6.winning_lights(['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500']) == 1000000 - 4

    assert day6.winning_lights_brightness(['turn on 0,0 through 0,0']) == 1
    assert day6.winning_lights_brightness(['toggle 0,0 through 999,999']) == 2000000

def test_day_7():
    data = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    ret = day7.run_circuit(data)
    assert ret['x'] == 123
    assert ret['y'] == 456
    assert ret['d'] == 72
    assert ret['e'] == 507
    assert ret['f'] == 492
    assert ret['g'] == 114
    assert ret['i'] == -457  # Unsigned: 65079
    assert ret['h'] == -124  # Unsigned: 65412

def test_day_8():
    assert day8.wasted_space([r'""']) == 2
    assert day8.wasted_space([r'"abc"']) == 2
    assert day8.wasted_space([r'"aaa\"aaa"']) == 3
    assert day8.wasted_space([r'"\x27"']) == 5
    assert day8.wasted_space([
        r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'
    ]) == 12
    assert day8.encode_wasted_space([r'""']) == 4
    assert day8.encode_wasted_space([r'"abc"']) == 4
    assert day8.encode_wasted_space([r'"aaa\"aaa"']) == 6
    assert day8.encode_wasted_space([r'"\x27"']) == 5
    assert day8.encode_wasted_space([
        r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'
    ]) == 19

def test_day_9():
    assert day9.santa_tsp([
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]) == 605

    assert day9.santa_tsp([
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ], comparison=max) == 982

def test_day_10():
    assert day10.look_and_say('1') == '11'
    assert day10.look_and_say('11') == '21'
    assert day10.look_and_say('21') == '1211'
    assert day10.look_and_say('1211') == '111221'
    assert day10.look_and_say('111221') == '312211'
    assert day10.look_and_say('1', iterations=5) == '312211'

def test_day_11():
    assert day11.is_valid('hijklmmn') is False
    assert day11.is_valid('abbceffg') is False
    assert day11.is_valid('abbcegjk') is False
    assert day11.is_valid('abcdffaa') is True
    assert day11.is_valid('ghjaabcc') is True
    assert day11.generate_password('abcdefgh') == 'abcdffaa'
    # This is very slow to generate
    # assert day11.generate_password('ghijklmn') == 'ghjaabcc'

def test_day_12():
    assert day12.json_sum('[1,2,3]') == 6
    assert day12.json_sum('{"a":2,"b":4}') == 6
    assert day12.json_sum('[[[3]]]') == 3
    assert day12.json_sum('{"a":{"b":4},"c":-1}') == 3
    assert day12.json_sum('{"a":[-1,1]}') == 0
    assert day12.json_sum('[-1,{"a":1}]') == 0
    assert day12.json_sum('[]') == 0
    assert day12.json_sum('{}') == 0

    assert day12.json_sum_not_red('[1,2,3]') == 6
    assert day12.json_sum_not_red('[1,{"c":"red","b":2},3]') == 4
    assert day12.json_sum_not_red('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert day12.json_sum_not_red('[1,"red",5]') == 6

def test_day_13():
    assert day13.optimize_happiness([
        'Alice would gain 54 happiness units by sitting next to Bob.',
        'Alice would lose 79 happiness units by sitting next to Carol.',
        'Alice would lose 2 happiness units by sitting next to David.',
        'Bob would gain 83 happiness units by sitting next to Alice.',
        'Bob would lose 7 happiness units by sitting next to Carol.',
        'Bob would lose 63 happiness units by sitting next to David.',
        'Carol would lose 62 happiness units by sitting next to Alice.',
        'Carol would gain 60 happiness units by sitting next to Bob.',
        'Carol would gain 55 happiness units by sitting next to David.',
        'David would gain 46 happiness units by sitting next to Alice.',
        'David would lose 7 happiness units by sitting next to Bob.',
        'David would gain 41 happiness units by sitting next to Carol.',
    ]) == 330

def test_day_14():
    assert day14.calc_distance([
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ], seconds=1000) == 1120

    assert day14.calc_points([
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ], seconds=1000) == 689

def test_day_15():
    od = collections.OrderedDict([
        ('butterscotch', {'capacity': -1, 'durability': -2, 'flavor': 6, 'texture': 3, 'calories': 8}),
        ('cinnamon', {'capacity': 2, 'durability': 3, 'flavor': -2, 'texture': -1, 'calories': 3})
    ])
    assert day15.calc_score(od, [44, 56]) == 62842880
    assert day15.make_best_cookie([
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    ]) == 62842880

    assert day15.calc_score(od, [44, 56], max_cal=500) == 0
    assert day15.calc_score(od, [40, 60], max_cal=500) == 57600000
    assert day15.make_best_cookie([
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
    ], max_cal=500) == 57600000

def test_day_17():
    assert day17.how_many_combinations(['20', '15', '10', '5', '5'], total=25) == 4
    assert day17.how_many_combinations(['20', '15', '10', '5', '5'], total=25, find_min=True) == 3

def test_day_18():
    assert day18.solve([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ], iterations=1) == 11
    assert day18.solve([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ], iterations=4) == 4
    assert day18.solve([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ], iterations=5, broken_lights=True) == 17

def test_day_19():
    assert day19.solve([
        'H => HO',
        'H => OH',
        'O => HH',
        '',
        'HOH',
    ]) == 4
    assert day19.solve([
        'HO => OH',
        'O => HH',
        '',
        'HOH',
    ]) == 2

def test_day_20():
    assert day20.solve('150') == 8
    assert day20.solve('100') == 6

def test_day_21():
    assert day21.run_game({'hp': 12, 'damage': 7, 'armor': 2}, {'hp': 8, 'damage': 5, 'armor': 5}) == 'player'

def test_day_23():
    assert day23.solve(['inc a', 'jio a, +2', 'tpl a', 'inc a'])['a'] == 2
