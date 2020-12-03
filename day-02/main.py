import os
import sys

def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [get_info(line) for line in f]
    return data

def get_info(line):
    chunks = line.strip().split(' ')
    range_ = chunks[0].split('-')
    letter = chunks[1].replace(':', '')
    pwd = chunks[2]
    return {
        'min': int(range_[0]),
        'max': int(range_[1]),
        'letter': letter,
        'password': pwd
    }

def is_valid(pwd_info, part):
    if part == 1:
        if (pwd_info['min'] <= pwd_info['password'].count(pwd_info['letter']) <=  pwd_info['max']):
            return True
        return False
    elif part == 2:
        found_in_pos1 = pwd_info['password'][pwd_info['min']-1] == pwd_info['letter']
        found_in_pos2 = pwd_info['password'][pwd_info['max']-1] == pwd_info['letter']
        if (found_in_pos1 and not found_in_pos2) or (found_in_pos2 and not found_in_pos1):
            return True
        return False
    else:
        raise ValueError(f'part has an unexpected value: {part}')
        

def get_result(part):
    valid_pwd_count = 0
    pwds = get_data()
    for pwd in pwds:
        if not is_valid(pwd, part):
            valid_pwd_count+=1
    return valid_pwd_count

print(get_result(1))
print(get_result(2))