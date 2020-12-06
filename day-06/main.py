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
        count = 0
        group = group.replace('\n', '')
        count += len(set(group))
        counts.append(count)
    return sum(counts)

def get_counts_2(data):
    counts = []
    groups = data.split("\n\n")
    for group in groups:
        count = 0
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
    print(f'part-1: {counts}')
    
# part 1 & 2
get_result()
