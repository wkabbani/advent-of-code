import os
import sys
from functools import reduce
from collections import Counter


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return f.read().strip()


def get_counts_1(data):
    counts = []
    groups = data.split("\n\n")
    for group in groups:
        group = group.replace('\n', '')
        counts.append(len(set(group)))
    return sum(counts)


def get_counts_2(data):
    counts = []
    groups = data.split("\n\n")
    for group in groups:
        persons = group.split('\n')
        counters = [Counter(person) for person in persons]
        res = reduce(lambda x, y: x & y, counters)
        counts.append(len(res))
    return sum(counts)


def get_result():
    data = get_data()
    counts = get_counts_1(data)
    print(f'part-1: {counts}')
    counts = get_counts_2(data)
    print(f'part-2: {counts}')


# part 1 & 2
get_result()
