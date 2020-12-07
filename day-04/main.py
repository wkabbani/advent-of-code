import os
import sys
import re


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def get_info(data):
    passports = []
    idx = 0
    while idx < len(data):
        pass_info = {}
        while idx < len(data) and data[idx] != '':
            chunks = data[idx].split(' ')
            for chunck in chunks:
                kv = chunck.split(':')
                pass_info[kv[0]] = kv[1]
            idx += 1
        idx += 1
        passports.append(pass_info)
    return passports


def is_valid_1(passport):
    if len(passport.keys()) == 8:
        return True
    elif (len(passport.keys()) == 7) and ('cid' not in passport.keys()):
        return True
    else:
        return False


def is_valid_hgt(hgt):
    sr = re.search("(\d+)(cm|in)", hgt)
    if sr:
        value = int(sr.group(1))
        unit = sr.group(2)
        if unit == 'cm' and (150 <= value <= 193):
            return True
        elif unit == 'in' and (59 <= value <= 76):
            return True
    return False


def is_valid_2(passport):
    if 'byr' not in passport or not (1920 <= int(passport['byr']) <= 2002):
        return False
    if 'iyr' not in passport or not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if 'eyr' not in passport or not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if 'hcl' not in passport or not (re.search("^#(?:[0-9a-f]{3}){1,2}$", passport['hcl'])):
        return False
    if 'ecl' not in passport or not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    if 'pid' not in passport or (not (len(passport['pid']) == 9)) or (not (passport['pid'].isnumeric())):
        return False
    if 'hgt' not in passport or not is_valid_hgt(passport['hgt']):
        return False
    return True


def get_result(part):
    n_valid = 0
    is_valid = is_valid_1 if part == 1 else is_valid_2
    passports = get_info(get_data())
    for pass_ in passports:
        if is_valid(pass_):
            n_valid += 1
    return n_valid


# part 1
print(get_result(1))

# # part 2
print(get_result(2))
