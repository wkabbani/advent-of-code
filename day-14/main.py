import os
import sys
import time
import math
import re
import itertools


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_program(data):
    program = []
    program_segment = {}
    for line in data:
        chunks = [x.strip() for x in line.split('=')]
        if chunks[0].startswith('mask'):
            if program_segment:
                program.append(program_segment.copy())
                program_segment.clear()
            program_segment['mask'] = chunks[1]
            program_segment['inst'] = []
        elif chunks[0].startswith('mem'):
            address = re.findall(
                r"\[\s*\+?(-?\d+)\s*\]", chunks[0])[0]
            value = int(chunks[1])
            program_segment['inst'].append((address, value))
    program.append(program_segment)
    return program


def number_to_bin_string(num):
    tmp1 = "{0:b}".format(num)
    return tmp1.rjust(36, "0")


def bin_string_to_num(b_num):
    return int(b_num, 2)


def apply_mask_to_value(b_num, mask):
    result = [char for char in b_num]
    for i, char in enumerate(mask):
        if char != 'X' and char.isnumeric():
            result[i] = char
    return ''.join(result)


def apply_mask_to_address(address, mask):
    result = [char for char in address]
    for i, char in enumerate(mask):
        if char in ('X', '1'):
            result[i] = char
    return ''.join(result)


def get_all_addresses(floating_address):
    result = []
    all_xs = [i for i, letter in enumerate(floating_address) if letter == 'X']
    if len(all_xs) == 0:
        return result.append(floating_address)
    lst = [list(i) for i in itertools.product([0, 1], repeat=len(all_xs))]
    for perm in lst:
        floating_address_copy = [char for char in floating_address]
        for i, idx in enumerate(all_xs):
            floating_address_copy[idx] = str(perm[i])
        result.append(''.join(floating_address_copy[:]))
    return result


def part_1(program):
    memory = {}
    for ps in program:
        for address, value in ps['inst']:
            memory[address] = bin_string_to_num(apply_mask_to_value(number_to_bin_string(
                value), ps['mask']))
    return sum(memory.values())


def part_2(program):
    memory = {}
    for ps in program:
        for address, value in ps['inst']:
            add_bin_str = number_to_bin_string(int(address))
            floating_address = apply_mask_to_address(add_bin_str, ps['mask'])
            all_addresses_bin = get_all_addresses(floating_address)
            all_addresses_num = [bin_string_to_num(
                b_add) for b_add in all_addresses_bin]
            for add in all_addresses_num:
                memory[add] = value
    return sum(memory.values())


def get_result():
    data = get_data()
    program = get_program(data)

    # part 1
    tic = time.perf_counter()
    res1 = part_1(program)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(program)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 12135523360904
# 2741969047858
get_result()
