#!/usr/bin/env python3
"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

"""
import os


def calc_points(data, seconds=2503):
    reindeer = {}
    for line in data:
        line = line.split()
        reindeer[line[0]] = {
            'rest': int(line[-2]),
            'speed': int(line[3]),
            'duration': int(line[6]),
            'resting': 0,
            'running': 0,
            'state': 'running'
        }

    points = {name: 0 for name in reindeer}
    distances = {name: 0 for name in reindeer}
    for _ in range(seconds):
        # Move reindeer
        for name, r in reindeer.items():
            if r['state'] == 'running':
                distances[name] += r['speed']
            r[r['state']] += 1
            if r['state'] == 'running' and r['running'] == r['duration']:
                r['state'] = 'resting'
                r['running'] = 0
            elif r['state'] == 'resting' and r['resting'] == r['rest']:
                r['state'] = 'running'
                r['resting'] = 0

        # Calc points
        furthest = max(distances.values())
        for name in reindeer:
            if distances[name] == furthest:
                points[name] += 1

    print('Points:', points)
    return max(points.values())

def calc_distance(data, seconds=2503):
    reindeer = {}
    for line in data:
        line = line.split()
        reindeer[line[0]] = {
            'rest': int(line[-2]),
            'speed': int(line[3]),
            'duration': int(line[6])
        }

    distances = {}
    for name, r in reindeer.items():
        cycle_time = r['rest'] + r['duration']
        num_cycles = seconds // cycle_time
        distance = num_cycles * r['speed'] * r['duration']
        cycle_leftover = seconds - (cycle_time * num_cycles)
        if cycle_leftover < r['duration']:
            distance += cycle_leftover * r['speed']
        else:
            distance += r['speed'] * r['duration']
        distances[name] = distance

    print('Distances:', distances)
    return max(distances.values())

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day14.input'), 'r') as f:
        data = f.read()
    data = data.splitlines()
    print('The winning reindeer travelled', calc_distance(data), 'km.')
    print('The winning reindeer earned', calc_points(data), 'points.')
