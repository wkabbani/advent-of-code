import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_instructions(data):
    instuctions = []
    for line in data:
        action = line[0]
        value = int(line[1:])
        instuctions.append((action, value))
    return instuctions


num_to_letter = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
letter_to_num = {'N': 0, 'E': 90, 'S': 180, 'W': 270}


def turn(cur_dir, turn, degrees):
    if turn == 'R':
        return num_to_letter[(letter_to_num[cur_dir] + degrees) % 360]
    elif turn == 'L':
        return num_to_letter[((letter_to_num[cur_dir] - degrees) % 360)]
    else:
        raise ValueError()


def rotate(horizontal, vertical, degree):
    if degree % 360 == 0:
        return horizontal, vertical
    elif degree % 360 == 90:
        return vertical, -horizontal
    elif degree % 360 == 180:
        return -horizontal, -vertical
    elif degree % 360 == 270:
        return -vertical, horizontal
    else:
        raise ValueError()


def part_1(instuctions):
    vertical, horizontal = 0, 0
    direction = 'E'

    for action, value in instuctions:

        if action == 'F':
            if direction == 'E':
                horizontal += value
            elif direction == 'W':
                horizontal -= value
            elif direction == 'N':
                vertical += value
            elif direction == 'S':
                vertical -= value
        elif action == 'N':
            vertical += value
        elif action == 'S':
            vertical -= value
        elif action == 'E':
            horizontal += value
        elif action == 'W':
            horizontal -= value
        elif action in ('R', 'L'):
            direction = turn(direction, action, value)

    return abs(vertical) + abs(horizontal)


def part_2(instuctions):
    ship_vertical, ship_horizontal = 0, 0
    vertical, horizontal = 1, 10

    for action, value in instuctions:
        if action == 'F':
            ship_vertical += value * vertical
            ship_horizontal += value * horizontal

        elif action == 'N':
            vertical += value
        elif action == 'S':
            vertical -= value
        elif action == 'E':
            horizontal += value
        elif action == 'W':
            horizontal -= value
        elif action == 'R':
            horizontal, vertical = rotate(horizontal, vertical, value)
        elif action == 'L':
            horizontal, vertical = rotate(horizontal, vertical, 360 - value)

    return abs(ship_vertical) + abs(ship_horizontal)


def get_result():
    data = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(get_instructions(data))
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(get_instructions(data))
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 445
# 42495
get_result()
