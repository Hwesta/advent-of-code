#!/usr/bin/env python
"""
--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----

Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:

    Only C is available, and so it is done first.
    Next, both A and F are available. A is first alphabetically, so it is done next.
    Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
    After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
    F is the only choice, so it is done next.
    Finally, E is completed.

So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?

--- Part Two ---

As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .
   1        C          .
   2        C          .
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE

Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these steps.

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?

"""
from __future__ import print_function
import collections
import os
import string
import typing as t


def get_next_choice(next_choices):
    """Get from next list in sorted order."""
    next_choices.sort(reverse=True)
    item = next_choices.pop()
    # print("item", item)
    return next_choices, item


def update_next_choices(item, steps, solution, next_choices):
    solution = set(solution)
    # Add to candidate next letters
    for k, v in steps.items():
        # If now satisfied
        # print('checking', k, v)
        if item in v["needs"] and v["needs"] <= solution:
            next_choices.append(k)
            # print('next choices', next_choices)
    return next_choices


def solve_part1(steps, next_choices):
    """Run each step immediately once the previous letters are complete"""
    # Run, add supports to update list if all deps done
    solution = []
    while next_choices:
        next_choices, item = get_next_choice(next_choices)
        solution.append(item)
        # print('solution', solution)

        # Add to candidate next letters
        next_choices = update_next_choices(item, steps, solution, next_choices)

    return ''.join(solution)


def solve_part2(steps, next_choices: t.List):
    # Workers is a list of workers (index = ID) and what letter they're doing
    workers = [None] * 2  # Test: 2, real: 5
    solution = []
    tick = -1
    tick_alert = collections.defaultdict(list)  # Alert that a worker is done on a tick

    # Run while there's more work to be done or at least one worker is busy
    while next_choices or any(workers):
        tick += 1
        # One loop is a tick
        # print('tick', tick)

        # Check who's done at this tick
        for worker_index in tick_alert[tick]:
            item = workers[worker_index]
            # print(f"worker {worker_index} finished {item}")
            solution.append(item)
            # print("solution", solution)
            workers[worker_index] = None
            next_choices = update_next_choices(item, steps, solution, next_choices)

        # # All workers busy, advance
        if workers.count(None) == 0:
            continue
        # Assign free workers new work
        for worker_index, letter in enumerate(workers):
            if letter is None and next_choices:
                # print(f"worker {worker_index} is free")
                next_choices, item = get_next_choice(next_choices)
                workers[worker_index] = item
                alert_tick = tick + string.ascii_uppercase.index(item) + 1 # + 60
                tick_alert[alert_tick].append(worker_index)
                # print(f"worker {worker_index} now working on {item} until {alert_tick}")
        if tick >= 500000:
            break

    return tick
    # 218 too low


def solve(data, flag=False):
    """Parse the data into needs/supports, run for each part"""
    def default_steps():
        return {"needs": set(), "supports": set()}
    # Generate graph of dependencies & supports
    steps = collections.defaultdict(default_steps)
    for row in data:
        row = row.split()
        before = row[1]
        after = row[-3]
        steps[before]["supports"].add(after)
        steps[after]["needs"].add(before)
    # print('steps', steps)

    # Find one with no deps
    next_choices = []
    for k, v in steps.items():
        if not v["needs"]:
            next_choices.append(k)

    if not flag:  # Part 1
        return solve_part1(steps, next_choices)
    else:
        return solve_part2(steps, next_choices)


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "day7.input")) as f:
        data = f.read().strip().splitlines()
    print("The order the steps are completed is", solve(data, False))
    print("The amount of time it takes with workers is", solve(data, True))
