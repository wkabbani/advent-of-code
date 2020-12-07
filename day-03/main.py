import os
import sys
import numpy as np


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_result(r_steps, d_steps):
    map_ = get_data()
    n_trees = 0
    r = 0
    c = 0
    while r < len(map_):
        c = (c + r_steps) % len(map_[r])
        r += d_steps
        if (r < len(map_) and map_[r][c] == '#'):
            n_trees += 1
    return n_trees


# part 1
print(get_result(3, 1))

# part 2
results = [get_result(s[0], s[1])
           for s in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(np.prod(results))
