#!/usr/bin/env python
"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

"""
import itertools
import os
import re

def real_room(room_id, checksum):
    sorted_id = sorted(room_id)
    calc_checksum = ''
    sorted_length = {}

    for key, group in itertools.groupby(sorted_id):
        if key == '-':
            continue
        sorted_length[key] = len(list(group))

    for key in sorted(sorted_length, key=lambda x: (-sorted_length[x], x)):
        calc_checksum += key
        if len(calc_checksum) == 5:
            break
    return calc_checksum == checksum

def rotate_room(room_id, sector_id):
    decrypted_id = ''
    rotate = sector_id % 26
    for character in room_id:
        if character == '-':
            decrypted_id += ' '
            continue
        # Only works with lowercase
        numeric = ord(character)
        numeric += rotate
        if numeric > ord('z'):
            numeric -= 26
        new_char = chr(numeric)
        decrypted_id += new_char

    return decrypted_id

def solve(data):
    regex = r'([\w-]+)-(\d+)\[(\w+)\]'
    count = 0
    for line in data:
        match = re.match(regex, line)
        if not match:
            print('error')
        room_id = match.group(1)
        sector = int(match.group(2))
        checksum = match.group(3)
        if real_room(room_id, checksum):
            count += sector
            rotated_room = rotate_room(room_id, sector)
            if rotated_room == 'northpole object storage':
                print('Room', room_id, 'sector', sector, 'contains', rotated_room)
    return count

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'day4.input')) as f:
        data = f.read().splitlines()
    print('There are', solve(data), 'valid rooms.')
