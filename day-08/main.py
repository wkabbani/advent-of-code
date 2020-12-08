import os
import sys
import time
from copy import deepcopy


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_code(data):
    code = []
    for line in data:
        chuncks = line.split(' ')
        inst = {}
        inst['ope'] = chuncks[0]
        inst['arg'] = int(chuncks[1])
        inst['exec'] = 0
        code.append(inst)
    return code


def get_acc(code):
    acc, loc = 0, 0
    while loc < len(code) and code[loc]['exec'] == 0:
        if code[loc]['ope'] == 'acc':
            code[loc]['exec'] += 1
            acc += code[loc]['arg']
            loc += 1
        elif code[loc]['ope'] == 'nop':
            code[loc]['exec'] += 1
            loc += 1
        else:  # 278
            code[loc]['exec'] += 1
            loc += code[loc]['arg']
    return acc, loc


def fix_get_acc(code):
    for i in range(0, len(code)):
        if code[i]['ope'] == 'acc':
            continue

        copy1 = deepcopy(code, memo=None, _nil=[])
        copy2 = deepcopy(code, memo=None, _nil=[])

        if code[i]['ope'] == 'jmp':
            copy2[i]['ope'] = 'nop'
        else:
            copy2[i]['ope'] = 'jmp'

        acc, loc = get_acc(copy1)
        if loc >= len(code):
            return acc

        acc, loc = get_acc(copy2)
        if loc >= len(code):
            return acc


def get_result():
    data = get_data()
    code = get_code(data)

    # part 1
    tic = time.perf_counter()
    acc, _ = get_acc(deepcopy(code, memo=None, _nil=[]))
    toc = time.perf_counter()
    print(f"Part-1: Counter: {acc}, took {toc - tic:0.4f} seconds")

    # part 1
    tic = time.perf_counter()
    acc = fix_get_acc(deepcopy(code, memo=None, _nil=[]))
    toc = time.perf_counter()
    print(f"Part-2: Counter: {acc}, took {toc - tic:0.4f} seconds")


# part 1 & 2
get_result()
