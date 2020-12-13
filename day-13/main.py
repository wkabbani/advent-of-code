import os
import sys
import time
import math
import numpy as np
from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable
from sympy.ntheory.modular import crt


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_notes(data):
    earliest_time = int(data[0])
    bus_ids = data[1].split(',')
    return earliest_time, bus_ids


def part_1(notes):
    filtered_bus_ids = [int(id) for id in notes[1] if id.isnumeric()]

    bus_times = []
    for bus_id in filtered_bus_ids:
        bus_times.append((bus_id, bus_id * math.ceil(notes[0] / bus_id)))
    bus_times.sort(key=lambda x: x[1])
    return bus_times[0][0] * (bus_times[0][1] - notes[0])


def part_2_v1(notes):
    """
    solving using lp
    builds a model and solves it using pulp, an lp package.
    solves the problem when the number of variables is very small, the basic examples, takes forever otherwise
    https://coin-or.github.io/pulp/
    """
    bus_offsets = []
    offset = 0
    for bus_id in notes[1]:
        if bus_id.isnumeric():
            bus_offsets.append((int(bus_id), offset))
        offset += 1
    return build_model_and_solve(bus_offsets)


def build_model_and_solve(bus_offsets):
    # Create the model
    model = LpProblem(name="small-problem", sense=LpMinimize)

    # Initialize the decision variables
    t = LpVariable(name="t", lowBound=0, cat="Integer")
    for i in range(len(bus_offsets)):
        vars()[f'x{i}'] = LpVariable(name=f'x{i}', lowBound=0, cat="Integer")

    # Add the constraints to the mode
    t_expression = -len(bus_offsets) * t
    for i in range(len(bus_offsets)):
        model += (bus_offsets[i][0] * vars()
                  [f'x{i}'] - bus_offsets[i][1] - t == 0, f'x{i}_constraint')
        t_expression = bus_offsets[i][0] * \
            vars()[f'x{i}'] - bus_offsets[i][1] + t_expression
    model += (t_expression == 0, f't_constraint')

    # Add the objective function to the model
    model += lpSum([t])

    # Solve the problem
    status = model.solve()

    # return t
    for var in model.variables():
        if var.name == 't':
            return var.varValue


def part_2_v2(notes, lower_bound_hint):
    """
    solves all the provided examples quickly, given a reasonable lower bound
    takes a lot of time for the real input
    """
    bus_offsets = []
    offset = 0
    for bus_id in notes[1]:
        if bus_id.isnumeric():
            bus_offsets.append((int(bus_id), offset))
        offset += 1

    max_bus_id = max([bo[0] for bo in bus_offsets])
    max_bus_tup = [tup for tup in bus_offsets if tup[0] == max_bus_id][0]

    lower_bound = math.ceil(lower_bound_hint / max_bus_id) * max_bus_id
    upper_bound = np.prod([bo[0] for bo in bus_offsets])

    near_min_ts = lower_bound
    while near_min_ts < upper_bound and not check_ok(max_bus_tup, near_min_ts, bus_offsets):
        near_min_ts += max_bus_id

    return near_min_ts - max_bus_tup[1]


def check_ok(max_bus_tup, near_min_ts, bus_offsets):
    for bus_id, offset in bus_offsets:
        if ((near_min_ts + (offset - max_bus_tup[1])) % bus_id) != 0:
            return False
    return True


def part_2_v3(notes):
    """
    uses chinese reminder theorem (https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
    just uses a package to calculate the crt
    """
    mods, rems = [], []
    for i in range(len(notes[1])):
        if notes[1][i].isnumeric():
            mods.append(int(notes[1][i]))
            rems.append((-i) % mods[-1])
    return crt(mods, rems)[0]


def get_result():
    data = get_data()
    notes = get_notes(data)

    # part 1
    tic = time.perf_counter()
    res1 = part_1(notes)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2 v1
    # tic = time.perf_counter()
    # res2 = part_2_v1(notes)
    # toc = time.perf_counter()
    # print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")

    # part 2 v2
    # tic = time.perf_counter()
    # res2 = part_2_v2(notes, 1000) # 1000 a lower bound hint for the examples
    # toc = time.perf_counter()
    # print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")

    # part 2 v3
    tic = time.perf_counter()
    res2 = part_2_v3(notes)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 4207
# 725850285300475
get_result()
