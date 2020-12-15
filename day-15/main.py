import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_starting_numbers(data):
    data = data[0].split(',')
    return [int(item.strip()) for item in data]


def part_1(starting_nums):
    turns = starting_nums[:]
    for i in range(len(starting_nums), 2020):
        try:
            reverse = turns[-2::-1]
            index_value = reverse.index(turns[-1])
            turns.append((i) - (len(turns) - index_value - 1))
        except ValueError:
            turns.append(0)
    return turns[-1]


def part_2(starting_nums):
    mem = {}
    for i in range(len(starting_nums)):
        mem[starting_nums[i]] = [-1, i+1]

    last_element = starting_nums[-1]
    for i in range(len(starting_nums)+1, 30_000_001):
        if last_element in mem.keys() and -1 not in mem[last_element]:
            new_element = mem[last_element][1] - mem[last_element][0]
            if new_element in mem.keys():
                mem[new_element] = [mem[new_element][1], i]
            else:
                mem[new_element] = [-1, i]
            last_element = new_element
        else:
            if 0 in mem.keys():
                mem[0] = [mem[0][1], i]
            else:
                mem[0] = [-1, i]
            last_element = 0
    return last_element


def get_result():
    data = get_data()
    starting_nums = get_starting_numbers(data)

    # part 1
    tic = time.perf_counter()
    res1 = part_1(starting_nums)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(starting_nums)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 257
# 8546398
get_result()
