import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def part_1(data):
    actives = set()
    for r, l in enumerate(data):
        for c, ch in enumerate(l):
            if ch == '#':
                actives.add((r, c, 0))

    for _ in range(6):
        new_on = set()
        for x in range(-10, 10):
            for y in range(-10, 10):
                for z in range(-10, 10):
                    nbr = 0
                    for dx in [-1, 0, +1]:
                        for dy in [-1, 0, +1]:
                            for dz in [-1, 0, +1]:
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x+dx, y+dy, z+dz) in actives:
                                        nbr += 1
                    if (x, y, z) not in actives and nbr == 3:
                        new_on.add((x, y, z))
                    if (x, y, z) in actives and nbr in (2, 3):
                        new_on.add((x, y, z))
        actives = new_on

    return len(actives)


def part_2(data):
    ON = set()
    for r, l in enumerate(data):
        for c, ch in enumerate(l):
            if ch == '#':
                ON.add((r, c, 0, 0))

    for _ in range(6):
        new_on = set()
        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-15, 15):
                    for w in range(-15, 15):
                        nbr = 0
                        for dx in [-1, 0, +1]:
                            for dy in [-1, 0, +1]:
                                for dz in [-1, 0, +1]:
                                    for dw in [-1, 0, +1]:
                                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                            if (x+dx, y+dy, z+dz, w+dw) in ON:
                                                nbr += 1
                        if (x, y, z, w) not in ON and nbr == 3:
                            new_on.add((x, y, z, w))
                        if (x, y, z, w) in ON and nbr in (2, 3):
                            new_on.add((x, y, z, w))
        ON = new_on

    return len(ON)


def get_result():
    data = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(data)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(data)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 372
# 1896
get_result()
