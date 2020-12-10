import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [int(line.strip()) for line in f]
    return data


def one_and_threes(data):
    ones = 0
    threes = 0
    current_joltage = 0
    for joltage in data:
        diff = joltage - current_joltage
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        current_joltage = joltage
    threes += 1
    return ones * threes


def get_distinct_ways(idx, data, n_ways):
    if idx == len(data)-1:
        return 1
    if idx in n_ways:
        return n_ways[idx]
    ways_count = 0
    for j in range(idx+1, idx+4):
        if j < len(data) and data[j]-data[idx] <= 3:
            ways_count += get_distinct_ways(j, data, n_ways)
    n_ways[idx] = ways_count
    return ways_count


def get_result():
    data = get_data()
    data.append(0)
    data.sort()

    # part 1
    tic = time.perf_counter()
    res1 = one_and_threes(data)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = get_distinct_ways(0, data, {})
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# part 1 & 2
# 1998
# 347250213298688
get_result()
