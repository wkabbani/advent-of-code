import os
import sys
import time
from copy import deepcopy


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    for i in range(0, len(data)):
        data[i] = list(data[i])
    return data


def get_immediate_occupied_seats(r, c, data):
    n_occupied = 0

    if r-1 >= 0 and data[r-1][c] == '#':
        n_occupied += 1
    if r+1 < len(data) and data[r+1][c] == '#':
        n_occupied += 1
    if c-1 >= 0 and data[r][c-1] == '#':
        n_occupied += 1
    if c+1 < len(data[r]) and data[r][c+1] == '#':
        n_occupied += 1

    if c-1 >= 0 and r-1 >= 0 and data[r-1][c-1] == '#':
        n_occupied += 1

    if c+1 < len(data[r]) and r+1 < len(data) and data[r+1][c+1] == '#':
        n_occupied += 1

    if c+1 < len(data[r]) and r-1 >= 0 and data[r-1][c+1] == '#':
        n_occupied += 1
    if c-1 >= 0 and r+1 < len(data) and data[r+1][c-1] == '#':
        n_occupied += 1

    return n_occupied


def get_line_of_sight_occupied_seats(row, col, data):
    n_occupied = 0
    directions = set()

    u, d, r, l = row-1, row+1, col+1, col-1

    while len(directions) < 8:

        if not(1 in directions) and u >= 0:
            if data[u][col] == '#':
                n_occupied += 1
                directions.add(1)
            elif data[u][col] == 'L':
                directions.add(1)
        else:
            directions.add(1)

        if not(2 in directions) and d <= len(data)-1:
            if data[d][col] == '#':
                n_occupied += 1
                directions.add(2)
            elif data[d][col] == 'L':
                directions.add(2)
        else:
            directions.add(2)

        if not(3 in directions) and r <= len(data[row])-1:
            if data[row][r] == '#':
                n_occupied += 1
                directions.add(3)
            elif data[row][r] == 'L':
                directions.add(3)
        else:
            directions.add(3)

        if not(4 in directions) and l >= 0:
            if data[row][l] == '#':
                n_occupied += 1
                directions.add(4)
            elif data[row][l] == 'L':
                directions.add(4)
        else:
            directions.add(4)

        if not(5 in directions) and u >= 0 and l >= 0:
            if data[u][l] == '#':
                n_occupied += 1
                directions.add(5)
            elif data[u][l] == 'L':
                directions.add(5)
        else:
            directions.add(5)

        if not(6 in directions) and d <= len(data)-1 and l >= 0:
            if data[d][l] == '#':
                n_occupied += 1
                directions.add(6)
            elif data[d][l] == 'L':
                directions.add(6)
        else:
            directions.add(6)

        if not(7 in directions) and u >= 0 and r <= len(data[row])-1:
            if data[u][r] == '#':
                n_occupied += 1
                directions.add(7)
            elif data[u][r] == 'L':
                directions.add(7)
        else:
            directions.add(7)

        if not(8 in directions) and d <= len(data)-1 and r <= len(data[row])-1:
            if data[d][r] == '#':
                n_occupied += 1
                directions.add(8)
            elif data[d][r] == 'L':
                directions.add(8)
        else:
            directions.add(8)

        u -= 1
        d += 1
        r += 1
        l -= 1

    return n_occupied


def get_occupied_seats(data, part):
    max_occupied_seats = 4 if part == 1 else 5
    get_occupied_seats = get_immediate_occupied_seats if part == 1 else get_line_of_sight_occupied_seats
    while True:
        copy = deepcopy(data)
        changes = False
        for i in range(0, len(copy)):
            for j in range(0, len(copy[i])):
                if copy[i][j] == '.':
                    continue
                if copy[i][j] == 'L' and get_occupied_seats(i, j, data) == 0:
                    copy[i][j] = '#'
                    changes = True
                elif copy[i][j] == '#' and get_occupied_seats(i, j, data) >= max_occupied_seats:
                    copy[i][j] = 'L'
                    changes = True
        data = copy
        first = False
        if not changes:
            break

    occupied_seats = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] == '#':
                occupied_seats += 1
    return occupied_seats


def get_result():
    data = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = get_occupied_seats(data, 1)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = get_occupied_seats(data, 2)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 2321
# 2102
# part 1 & 2
get_result()
