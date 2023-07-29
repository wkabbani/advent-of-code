import os
import sys
import time


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = [line.strip() for line in f]

    food = []
    for line in data:
        contains = line.index('(')
        ingredients = [ingredient.strip()
                       for ingredient in line[:contains].split()]
        allergens = [allergen.strip() for allergen in line[contains:].replace(
            '(contains', '').replace(')', '').split(',')]
        food.append((ingredients, allergens))

    return food


def get_ingredients_allergens(food_list):
    result = {}
    for ingredients, allergens in food_list:
        for ingredient in ingredients:
            if ingredient not in result:
                result[ingredient] = set(allergens)
            else:
                result[ingredient] = result[ingredient].union(set(allergens))
    return result


def check(food_list, ingredient, allergen):
    for ingredients, allergens in food_list:
        if (ingredient not in ingredients) and (allergen in allergens):
            return True
    return False


def part_1(food_list, ing_all_list):
    ing_list = []
    for ingredient, allergens in ing_all_list.items():
        should_add = True
        for allergen in allergens:
            if not check(food_list, ingredient, allergen):
                should_add = False
        if should_add:
            ing_list.append(ingredient)

    count = 0
    ing_list = list(set(ing_list))
    for ingredient in ing_list:
        for ingredients, _ in food_list:
            count += ingredients.count(ingredient)

    return count, ing_list


def part_2(food_list, ing_all_list, inert):
    all_allergens = set()
    for _, v in ing_all_list.items():
        all_allergens.update(v)
    print(list(all_allergens))

    dangerous_ing = ing_all_list.keys() - inert

    dang_ing_counts = {}
    for dan_ing in dangerous_ing:
        dang_ing_counts[dan_ing] = []

    allergen_counts = {}
    for allergen in all_allergens:
        allergen_counts[allergen] = []

    for idx, (ingredients, allergens) in enumerate(food_list):
        for ing in dangerous_ing:
            if ing in ingredients:
                dang_ing_counts[ing].append(idx)

        for all in all_allergens:
            if all in allergens:
                allergen_counts[all].append(idx)

    for k, v in allergen_counts.items():
        print(k, v)
        for k1, v1 in dang_ing_counts.items():
            if len(set(v) - set(v1)) == 0:
                print(k1)


def get_result():
    food_list = get_data()
    ing_all_list = get_ingredients_allergens(food_list)
    # print(food_list)
    # print(food_list)

    # part 1
    tic = time.perf_counter()
    res1, inert = part_1(food_list, ing_all_list)
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    tic = time.perf_counter()
    res2 = part_2(food_list, ing_all_list, inert)
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")

    tmp = sorted(['dairy', 'nuts', 'soy', 'eggs',
                  'shellfish', 'fish', 'peanuts', 'sesame'])
    print(tmp)


# 140656720229539
# qqskn,ccvnlbp,tcm,jnqcd,qjqb,xjqd,xhzr,cjxv
get_result()
