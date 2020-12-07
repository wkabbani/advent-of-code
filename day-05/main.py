import os
import sys
import math


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_seat_ids(data):
    seat_ids = []
    for seat_str in data:
        r_min, r_max = 0, 127
        c_min, c_max = 0, 7
        for i in range(6):
            if seat_str[i] == 'F':
                r_max = (r_min + r_max) // 2
            else:
                r_min = math.ceil((r_min + r_max) / 2)
        for i in range(7, 9):
            if seat_str[i] == 'L':
                c_max = (c_min + c_max) // 2
            else:
                c_min = math.ceil((c_min + c_max) / 2)
        row = r_min if seat_str[6] == 'F' else r_max
        col = c_min if seat_str[9] == 'L' else c_max
        seat_ids.append(row * 8 + col)
    return seat_ids


def get_seat_id(seat_ids):
    full_range = list(range(0, 1024, 1))
    potential_seats = list(set(full_range) - set(seat_ids))
    for seat in potential_seats:
        if (seat - 1) in seat_ids and (seat + 1) in seat_ids:
            return seat  # assume there is only one


def get_result():
    seat_ids = get_seat_ids(get_data())

    print(f'part-1: {max(seat_ids)}')

    print(f'part-2: {get_seat_id(seat_ids)}')


# part 1 & 2
get_result()
