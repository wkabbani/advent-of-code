import os
import sys
import time
import numpy as np


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_all_possible_forms(tile):
    return [
        tile.copy(), np.rot90(tile, 1),
        np.rot90(tile, 2), np.rot90(tile, 3),
        np.flip(tile, 0), np.flip(tile, 1),
        np.flip(np.rot90(tile, 1), 0), np.flip(np.rot90(tile, 1), 1)
    ]


def get_tiles(data):
    tiles = {}
    tile_id = -1
    tile = []
    for line in data:
        if line.startswith('Tile'):
            chunks = line.split()
            tile_id = chunks[1].replace(':', '')
        elif line != '':
            tile.append([ch for ch in line])
        elif line == '':
            for i, form in enumerate(get_all_possible_forms(np.array(tile))):
                tiles[int(tile_id) * (pow(10, i))] = {}
                tiles[int(tile_id) * (pow(10, i))]['data'] = form
            tile.clear()

    for i, form in enumerate(get_all_possible_forms(np.array(tile))):
        tiles[int(tile_id) * (pow(10, i))] = {}
        tiles[int(tile_id) * (pow(10, i))]['data'] = form
    return tiles


def match_bottom(a, b):
    # last line in a matches first line in b
    # a
    # b
    return (a[-1, :] == b[0, :]).all()


def match_top(a, b):
    # first line in a matches last line in b
    # b
    # a
    return (b[-1, :] == a[0, :]).all()


def match_right(a, b):
    # last col in a matches first col in b
    # a b
    return (a[:, -1] == b[:, 0]).all()


def match_left(a, b):
    # first col in a matches last col in b
    # b a
    return (a[:, 0] == b[:, -1]).all()


def get_matches(tile, other_tile):
    bottom = match_bottom(tile, other_tile)
    top = match_top(tile, other_tile)
    right = match_right(tile, other_tile)
    left = match_left(tile, other_tile)

    if bottom:
        return 'b'
    if top:
        return 't'
    if right:
        return 'r'
    if left:
        return 'l'

    return ''


reverse_match_dict = {'t': 'b', 'b': 't', 'l': 'r', 'r': 'l'}


def part_1(tiles):
    for tile in tiles:
        for other_tile in tiles:
            if other_tile not in [tile, tile*10, tile*100, tile*1000, tile*10000, tile*100000, tile*1000000, tile*10000000]:
                match_result = get_matches(
                    tiles[tile]['data'], tiles[other_tile]['data'])
                if match_result != '':
                    tiles[tile][match_result] = other_tile
                    tiles[other_tile][reverse_match_dict[match_result]] = tile

    corners = []
    for k, v in tiles.items():
        if len(v.keys())-1 == 2:
            corners.append(k)

    corners = set([int(str(k).strip('0')) for k in corners])
    return np.prod(np.array(list(corners)), axis=0)


def part_2(tiles):
    pass


def get_result():
    data = get_data()
    tiles = get_tiles(data)

    # part 1
    tic = time.perf_counter()
    res1 = part_1(tiles)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    # tic = time.perf_counter()
    # res2 = part_2(data)
    # toc = time.perf_counter()
    # print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 140656720229539
#
get_result()
