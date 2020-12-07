import os
import sys


class Color:
    def __init__(self, name):
        self.contains = {}
        self.contained = {}
        self.name = name

    def get_contained(self):
        return self.contained

    def get_contains(self):
        return self.contains


class Rules:
    def __init__(self):
        self.colors = {}

    def contains(self, color):
        if color in self.colors:
            return True
        return False

    def add(self, color):
        if color not in self.colors:
            self.colors[color] = Color(color)

    def add_relation(self, ocolor, icolor, count):
        self.add(ocolor)
        self.add(icolor)
        self.colors[ocolor].contains[icolor] = count
        self.colors[icolor].contained[ocolor] = count


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_rules(data):
    rules = Rules()
    for line in data:
        line = line.replace('.', '').strip()
        chuncks = line.split('contain')
        ocolor = chuncks[0].replace('bags', '').strip()
        rules.add(ocolor)
        if 'no other' not in chuncks[1]:
            ichunks = chuncks[1].split(',')
            for ichunck in ichunks:
                count_color = ichunck.replace(
                    'bags', '').replace('bag', '').strip()
                icount = int(count_color[0])
                icolor = count_color[1:].strip()
                rules.add_relation(ocolor, icolor, icount)
    return rules


def get_eventual_colors(color, rules):
    colors = []
    if rules.contains(color):
        parents = rules.colors[color].get_contained()
        colors.extend(parents.keys())
        for parent in parents.keys():
            colors.extend(get_eventual_colors(parent, rules))
    return colors


def get_inner_bags_count(color, rules):
    count = 0
    if rules.contains(color):
        childs = rules.colors[color].get_contains()
        count = sum(childs.values())
        for child in childs.keys():
            count += (get_inner_bags_count(child, rules) * childs[child])
    return count


def get_result():
    data = get_data()
    rules = get_rules(data)

    # part 1
    ev = get_eventual_colors('shiny gold', rules)
    print(f'Part-1: {len(set(ev))}')

    count = get_inner_bags_count('shiny gold', rules)
    print(f'Part-2: {count}')


# part 1 & 2
get_result()
