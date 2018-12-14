#!/usr/bin/env python
"""
--- Day 8: Memory Maneuver ---

The sleigh is much easier to pull than you'd expect for something its weight. Unfortunately, neither you nor the Elves know which way the North Pole is from here.

You check your wrist device for anything that might help. It seems to have some kind of navigation system! Activating the navigation system produces more bad news: "Failed to start navigation system. Could not read software license file."

The navigation system's license file consists of a list of numbers (your puzzle input). The numbers define a data structure which, when processed, produces some kind of tree that can be used to calculate the license number.

The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in the tree (or contains nodes that contain nodes, and so on).

Specifically, a node consists of:

    A header, which is always exactly two numbers:
        The quantity of child nodes.
        The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).

Each child node is itself a node that has its own header, child nodes, and metadata. For example:

2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

In this example, each node of the tree is also marked with an underline starting with a letter for easier identification. In it, there are four nodes:

    A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
    B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
    C, which has 1 child node (D) and 1 metadata entry (2).
    D, which has 0 child nodes and 1 metadata entry (99).

The first check done on the license file is to simply add up all of the metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

What is the sum of all metadata entries?

"""
from __future__ import print_function
import os

metadata_value = 0


def parse_node(node):
    """Recursively parse a node's header, metadata & children"""
    global metadata_value
    # print('new node', node)
    child_count = node[0]
    metadata_count = node[1]
    parsed = 2
    # print(f"child count: {child_count}, metadata count: {metadata_count}")
    # print("children", node[2:])

    children = []
    for _ in range(child_count):
        # print("parse child from", node[parsed:])
        child = parse_node(node[parsed:])
        parsed += child["len"]
        children.append(child)
    # children = parse_node(node[2:-metadata_count])

    metadata = node[parsed:parsed + metadata_count]
    metadata_value += sum(metadata)

    length = parsed + metadata_count
    node_info = {"len": length, "child_count": child_count, "metadata_count": metadata_count, "metadata": metadata, "children": children}
    # print('node info', node_info)
    return node_info


def solve(data, flag=False):
    data = list(map(int, data.split()))
    parse_node(data)

    return metadata_value


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "day8.input")) as f:
        data = f.read().strip()
    print(solve(data, False))
    # print(solve(data, True))
