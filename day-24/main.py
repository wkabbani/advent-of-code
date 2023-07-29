import os
import sys
import time
from collections import deque, namedtuple

_Hex = namedtuple("Hex", ["x", "y", "z"])


def Hex(x, y, z):
    assert not (round(x + y + z) != 0), "x + y + z must be 0"
    return _Hex(x, y, z)


def hex_add(a, b):
    return Hex(a.x + b.x, a.y + b.y, a.z + b.z)


hex_directions = [
    Hex(+1, -1, 0), Hex(+1, 0, -1), Hex(0, +1, -1),
    Hex(-1, +1, 0), Hex(-1, 0, +1), Hex(0, -1, +1),
]

dir_str_to_ind = {
    'e': 0,
    'se': 5,
    'sw': 4,
    'w': 3,
    'nw': 2,
    'ne': 1
}


def hex_direction(direction):
    return hex_directions[direction]


def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))


def hex_neighbors(hex) -> set:
    neighbors = set()
    for dir_str in dir_str_to_ind:
        neighbors.add(hex_neighbor(hex, dir_str_to_ind[dir_str]))
    assert len(neighbors) == 6, "every tile must have 6 neighbors"
    return neighbors


def hex_path(hex, path):
    end_tile = hex
    for dir_str in path:
        end_tile = hex_neighbor(end_tile, dir_str_to_ind[dir_str])
    return end_tile


def get_data():
    lines = []
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = f.readlines()
    return [parse_line(line.strip()) for line in data]


def parse_line(line):
    path = []
    while line:
        if line.startswith('ne'):
            line = line[2:]
            path.append('ne')
        elif line.startswith('nw'):
            line = line[2:]
            path.append('nw')
        elif line.startswith('se'):
            line = line[2:]
            path.append('se')
        elif line.startswith('sw'):
            line = line[2:]
            path.append('sw')
        elif line.startswith('e'):
            line = line[1:]
            path.append('e')
        elif line.startswith('w'):
            line = line[1:]
            path.append('w')
        else:
            raise Exception()
    return path


def part_1(paths):
    black_tiles = set()
    white_tiles = set()
    start_tile = Hex(0, 0, 0)
    white_tiles.add(start_tile)

    for path in paths:
        end_tile = hex_path(start_tile, path)
        white_tiles.add(end_tile)
        if end_tile in black_tiles:
            black_tiles.remove(end_tile)
        else:
            black_tiles.add(end_tile)

    return white_tiles-black_tiles, black_tiles, len(black_tiles)


def part_2(white_tiles, black_tiles):
    print(len(black_tiles))
    print(len(white_tiles))
    all_white_tiles = white_tiles.copy()

    for tile in black_tiles:
        neighbors = hex_neighbors(tile)
        all_white_tiles.update(neighbors)

    for tile in white_tiles:
        neighbors = hex_neighbors(tile)
        all_white_tiles.update(neighbors)

    white_tiles = all_white_tiles.copy()
    for tile in all_white_tiles:
        neighbors = hex_neighbors(tile)
        white_tiles.update(neighbors)

    print(len(black_tiles))
    print(len(white_tiles))
    total = len(black_tiles) + len(white_tiles)
    print('----------------')

    for day in range(0, 100):
        todays_blacks = set()
        todays_whites = set()

        for tile in black_tiles:
            all_neighbors = hex_neighbors(tile)
            black_neighbors = len(all_neighbors & black_tiles)
            if black_neighbors == 0 or black_neighbors > 2:
                todays_whites.add(tile)
            else:
                todays_blacks.add(tile)

        for tile in white_tiles:
            all_neighbors = hex_neighbors(tile)
            black_neighbors = len(all_neighbors & black_tiles)
            if black_neighbors == 2:
                todays_blacks.add(tile)
            else:
                todays_whites.add(tile)

        black_tiles = todays_blacks.copy()
        white_tiles = todays_whites.copy()

        all_white_tiles = white_tiles.copy()
        for tile in black_tiles:
            neighbors = hex_neighbors(tile)
            all_white_tiles.update(neighbors)

        for tile in white_tiles:
            neighbors = hex_neighbors(tile)
            all_white_tiles.update(neighbors)

        white_tiles = all_white_tiles.copy()
        for tile in all_white_tiles:
            neighbors = hex_neighbors(tile)
            white_tiles.update(neighbors)

        print(len(black_tiles))
        print(len(white_tiles))
        # assert total == len(black_tiles) + len(white_tiles)
        print(f'Day {day+1}: {len(black_tiles)}')

    return len(black_tiles)


def get_result():
    paths = get_data()

    # part 1
    tic = time.perf_counter()
    white_tiles, black_tiles, res1 = part_1(paths)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    tic = time.perf_counter()
    res2 = part_2(white_tiles, black_tiles)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")

    # 34664
    # 32018
get_result()
