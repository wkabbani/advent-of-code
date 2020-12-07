import os
import sys


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [int(line.strip()) for line in f]
    return lines


def get_result_1(target_sum):
    entries = get_data()
    hash_map = {}

    for i in range(len(entries)):
        hash_map[entries[i]] = i

    for i in range(len(entries)):
        if (target_sum - entries[i]) in hash_map and hash_map[target_sum - entries[i]] != i:
            return entries[i] * (target_sum - entries[i])


def get_result_2(target_sum):
    entries = get_data()
    hash_map = {}

    for i in range(len(entries)):
        hash_map[entries[i]] = i

    for i in range(len(entries)):
        partial_target_sum = target_sum - entries[i]
        for j in range(i + 1, len(entries)):
            if (partial_target_sum - entries[j]) in hash_map and hash_map[partial_target_sum - entries[j]] != j:
                return entries[i] * entries[j] * (partial_target_sum - entries[j])


print(get_result_1(2020))
print(get_result_2(2020))
