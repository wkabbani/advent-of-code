import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]

    rules = {}
    messages = []
    read_rules = True

    for line in data:
        if line == '':
            read_rules = False
            continue

        if read_rules:
            chunks = line.split(': ')
            if '"' in chunks[1]:
                rules[int(chunks[0])] = chunks[1][1:].replace('"', '').strip()
            else:
                sub_rules = chunks[1].split(' | ')
                tmp = []
                for sr in sub_rules:
                    tmp.append([int(v) for v in sr.split(' ')])
                rules[int(chunks[0])] = tmp

        else:
            messages.append(line)

    return rules, messages


def match(rules, message, rule):
    if len(rule) > len(message):
        return False

    if len(rule) == 0 and len(message) > 0:
        return False

    if len(rule) == 0 and len(message) == 0:
        return True

    if rule[0] in ('a', 'b'):
        if message[0] == rule[0]:
            return match(rules, message[1:], rule[1:])
    else:
        for sub_rule in rules[rule[0]]:
            if sub_rule in ('a', 'b'):
                sub_rule = [sub_rule]
            if match(rules, message, sub_rule + rule[1:]):
                return True

    return False


def part_1(rules, messages):
    count = 0
    for message in messages:
        if match(rules, message, rules[0][0]):
            count += 1
    return count


def part_2(rules, messages):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    count = 0
    for message in messages:
        if match(rules, message, rules[0][0]):
            count += 1
    return count


def get_result():
    rules, messages = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(rules, messages)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(rules, messages)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 195
# 309
get_result()
