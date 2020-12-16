import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_fields(data):
    fields = []
    for line in data:
        if not line:
            break
        field = {}
        # name
        chunks = line.split(':')
        field['name'] = chunks[0].strip()
        # ranges
        chunks = chunks[1].strip().split('or')
        range1 = chunks[0].strip().split('-')
        range2 = chunks[1].strip().split('-')
        ranges = []
        ranges.append((int(range1[0].strip()), int(range1[1].strip())))
        ranges.append((int(range2[0].strip()), int(range2[1].strip())))
        field['ranges'] = ranges
        fields.append(field.copy())
    return fields


def get_my_ticket(data):
    found = False
    my_ticket = []
    for line in data:
        if not found and line.startswith('your ticket'):
            found = True
            continue
        if found:
            my_ticket = [int(value) for value in line.split(',')]
            break
    return my_ticket


def get_nearby_tickets(data):
    found = False
    nearby_tickets = []
    for line in data:
        if not found and line.startswith('nearby ticket'):
            found = True
            continue
        if found:
            nearby_tickets.append([int(value) for value in line.split(',')])
    return nearby_tickets


def get_error_rate_for_ticket(fields, ticket, default_value=0):
    for value in ticket:
        valid = False
        for field in fields:
            if (field['ranges'][0][0] <= value <= field['ranges'][0][1]) or (field['ranges'][1][0] <= value <= field['ranges'][1][1]):
                valid = True
        if not valid:
            return value
    return default_value


def get_valid_tickets(fields, nearby_tickets):
    result = []
    for nearby_ticket in nearby_tickets:
        if get_error_rate_for_ticket(fields, nearby_ticket, default_value=-1) == -1:
            result.append(nearby_ticket)
    return result


def get_fields_cols(fields, nearby_tickets):
    valid_tickets = get_valid_tickets(fields, nearby_tickets)
    fields_cols = []
    for field in fields:
        field_cols = {'name': field['name'], 'cols': []}
        for c in range(0, 20):
            column = [nearby_ticket[c] for nearby_ticket in valid_tickets]
            if get_error_rate_for_ticket([field], column, default_value=-1) == -1:
                field_cols['cols'].append(c)
        fields_cols.append(field_cols.copy())

    last_checked = ''
    for i in range(0, 20):
        for fc1 in fields_cols:
            if len(fc1['cols']) == 1 and fc1['name'] != last_checked:
                last_checked = fc1['name']
                for fc2 in fields_cols:
                    if fc2['name'] != fc1['name']:
                        if fc1['cols'][0] in fc2['cols']:
                            fc2['cols'].remove(fc1['cols'][0])

    return fields_cols


def part_1(fields, nearby_tickets):
    error_rate = 0
    for nearby_ticket in nearby_tickets:
        error_rate += get_error_rate_for_ticket(fields, nearby_ticket)
    return error_rate


def part_2(fields, nearby_tickets, my_ticket):
    fields_cols = get_fields_cols(fields, nearby_tickets)
    result = 1
    for fc in fields_cols:
        if fc['name'].startswith('departure'):
            result *= my_ticket[fc['cols'][0]]
    return result


def get_result():
    data = get_data()
    fields = get_fields(data)
    my_ticket = get_my_ticket(data)
    nearby_tickets = get_nearby_tickets(data)

    # part 1
    tic = time.perf_counter()
    res1 = part_1(fields, nearby_tickets)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(fields, nearby_tickets, my_ticket)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 20058
# 366871907221
get_result()
