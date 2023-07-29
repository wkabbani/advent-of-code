import os
import sys
import time
from collections import deque


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = f.readlines()
    return [int(pk.strip()) for pk in data]


def get_loop_size(pk):
    value = 1
    lp = 0
    while value != pk:
        value = (value * 7) % 20201227
        lp += 1
    return lp


def transform(lp, pk):
    value = 1
    for _ in range(lp):
        value = (value * pk) % 20201227
    return value


def part_1(pks):
    card_pk, door_pk = pks[0], pks[1]

    card_lp = get_loop_size(card_pk)
    door_lp = get_loop_size(door_pk)

    key1 = transform(card_lp, door_pk)
    key2 = transform(door_lp, card_pk)

    assert key1 == key2
    return key1


def get_result():
    pks = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(pks)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    # tic = time.perf_counter()
    # res2 = part_2(p1_deck.copy(), p2_deck.copy())
    # toc = time.perf_counter()
    # print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 34664
# 32018
get_result()
