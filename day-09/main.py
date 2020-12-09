import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [int(line.strip()) for line in f]
    return data


def is_valid(target_sum, entries):
    hash_map = {}

    for i in range(len(entries)):
        hash_map[entries[i]] = i

    for i in range(len(entries)):
        if (target_sum - entries[i]) in hash_map and hash_map[target_sum - entries[i]] != i:
            return True
    return False


def get_number(data):
    i = 25
    while i < len(data):
        if not is_valid(data[i], data[i-25:i]):
            print(i)
            return data[i]
        i += 1


def get_weakness(data, target):
    for i in range(0, len(data)-1):
        sum = data[i]
        nums = [data[i]]
        for j in range(i+1, len(data)):
            sum += data[j]
            nums.append(data[j])
            if sum == target:
                return nums
            elif sum < target:
                continue
            else:
                break


# 85848519

def get_result():
    data = get_data()

    # part 1
    tic = time.perf_counter()
    number = get_number(data)
    toc = time.perf_counter()
    print(f"Part-1: Number: {number}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    nums = get_weakness(data, number)
    toc = time.perf_counter()
    print(
        f"Part-2: Weakness: {max(nums) + min(nums)}, took {toc - tic:0.4f} seconds")


# part 1 & 2
get_result()
