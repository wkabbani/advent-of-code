import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]
    return data


def evaluate_simple_expression(expression):
    result = 0
    operator = ''
    for ch in expression:
        if (type(ch) == int or ch.isnumeric()) and operator == '':
            result += int(ch)
        elif (type(ch) == int or ch.isnumeric()) and operator == '+':
            result += int(ch)
        elif (type(ch) == int or ch.isnumeric()) and operator == '*':
            result *= int(ch)
        elif ch in ('+', '*'):
            operator = ch
    return result


def evaluate_expression_with_addition(expression):
    expression = [element for element in expression if element != ' ']
    all_occurrences = [index for index,
                       element in enumerate(expression) if element == '+']
    idx = all_occurrences[0] if len(all_occurrences) > 0 else -1
    while idx != -1:
        expression[idx] = int(expression[idx-1]) + int(expression[idx+1])
        del expression[idx-1]
        del expression[idx]
        all_occurrences = [index for index,
                           element in enumerate(expression) if element == '+']
        idx = all_occurrences[0] if len(all_occurrences) > 0 else -1

    return evaluate_simple_expression(expression)


def evaluate_expression_with_parantheses(expression, part1=True):
    sub_evaluator = evaluate_simple_expression if part1 else evaluate_expression_with_addition
    stack = []
    for ch in expression:
        if ch == ')':
            sub_exp = []
            other = stack.pop()
            while other != '(':
                sub_exp.insert(0, other)
                other = stack.pop()
            stack.append(sub_evaluator(sub_exp))
        elif ch != ' ':
            stack.append(ch)
    return sub_evaluator(stack)


def part_1(data):
    result = 0
    for line in data:
        result += evaluate_expression_with_parantheses(line)
    return result


def part_2(data):
    result = 0
    for line in data:
        result += evaluate_expression_with_parantheses(line, part1=False)
    return result


def get_result():
    data = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(data)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # part 2
    tic = time.perf_counter()
    res2 = part_2(data)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 1408133923393
# 314455761823725
get_result()
