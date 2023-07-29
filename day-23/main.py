import os
import sys
import time
from collections import deque


class DLLNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.prev = None


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = f.read()
    return deque([int(cup) for cup in data])


def simulate_move(cups, current_cup_idx):

    # print(cups)

    # current & dest cups
    current_cup_lbl = cups[current_cup_idx]
    destination_cup_lbl = current_cup_lbl - 1
    # print(current_cup_lbl, current_cup_idx)

    cups.rotate(-1-current_cup_idx)

    # pick up cups
    picked_up_cups = []
    picked_up_cups.append(cups.popleft())
    picked_up_cups.append(cups.popleft())
    picked_up_cups.append(cups.popleft())

    # print(cups)

    # selecting a destination cup
    while picked_up_cups.count(destination_cup_lbl) > 0 and destination_cup_lbl >= min(cups):
        destination_cup_lbl -= 1

    if destination_cup_lbl < min(cups):
        destination_cup_lbl = max(cups)

    destination_cup_idx = cups.index(destination_cup_lbl)
    # print(destination_cup_lbl, destination_cup_idx)

    # placing the picked up cups
    cups.insert(destination_cup_idx+1, picked_up_cups[0])
    cups.insert(destination_cup_idx+2, picked_up_cups[1])
    cups.insert(destination_cup_idx+3, picked_up_cups[2])

    cups.rotate(1+current_cup_idx)

    # print(cups)

    return cups, (current_cup_idx+1) % len(cups)


def part_1(cups):
    cups, idx = simulate_move(cups, 0)
    for _ in range(99):
        cups, idx = simulate_move(cups, idx)

    # print(cups)
    cups.rotate(-cups.index(1))
    # print(cups)
    return ''.join([str(i) for i in list(cups)[1:]])


def get_dll(cups):
    prev_node = None
    first = True
    first_node = None
    for cup in cups:
        node = DLLNode(cup)
        if first:
            first_node = node
            first = False
        if prev_node:
            node.prev = prev_node
            prev_node.next = node
        prev_node = node

    first_node.prev = prev_node
    prev_node.next = first_node

    return first_node


def LargestInDLL(head_ref):

    max = None
    temp = None

    """ initialize two pointer temp
    and max on the head node """
    temp = max = head_ref
    temp = head_ref.next

    # traverse the whole doubly linked list
    while (temp.label != head_ref.label):

        """ if temp's data is greater than
        max's data, then put max = temp
        and return max.data """
        if (temp.label > max.label):
            max = temp

        temp = temp.next

    return max


def simulate_move_dll(first: DLLNode, current_cup: DLLNode):

    print_dll(first)

    # current & dest cups
    current_cup_lbl = current_cup.label
    destination_cup_lbl = current_cup_lbl - 1

    # cups.rotate(-1-current_cup_idx)

    # pick up cups
    picked_up_cups = []
    pick_up_cups_ptr = current_cup.next
    picked_up_cups.append(pick_up_cups_ptr.label)
    pick_up_cups_ptr = pick_up_cups_ptr.next

    picked_up_cups.append(pick_up_cups_ptr.label)
    pick_up_cups_ptr = pick_up_cups_ptr.next

    picked_up_cups.append(pick_up_cups_ptr.label)
    pick_up_cups_ptr = pick_up_cups_ptr.next

    print(picked_up_cups)

    # remove them
    current_cup.next = pick_up_cups_ptr
    pick_up_cups_ptr.prev = current_cup

    # # selecting a destination cup
    while picked_up_cups.count(destination_cup_lbl) > 0 and destination_cup_lbl >= 1:
        destination_cup_lbl -= 1

    destination_cup_idx = first
    if destination_cup_lbl >= 1:
        while(destination_cup_idx.label != destination_cup_lbl):
            destination_cup_idx = destination_cup_idx.next
    else:
        destination_cup_idx = LargestInDLL(first)

    print(destination_cup_idx.label)

    # # placing the picked up cups
    save_next = destination_cup_idx.next

    node1 = DLLNode(picked_up_cups[0])
    node2 = DLLNode(picked_up_cups[1])
    node3 = DLLNode(picked_up_cups[2])

    destination_cup_idx.next = node1
    node1.prev = destination_cup_idx

    node1.next = node2
    node2.prev = node1

    node2.next = node3
    node3.prev = node2

    node3.next = save_next
    save_next.prev = node3

    # cups.rotate(1+current_cup_idx)

    tmp = first
    rotate = False
    while(tmp.label != current_cup.label):
        if tmp.label == destination_cup_idx.label:
            rotate = True
        tmp = tmp.next

    if rotate:
        first = first.next.next.next

    print_dll(first)

    return first, current_cup.next
    # return cups, (current_cup_idx+1) % len(cups)


def print_dll(first):
    ptr = first
    print(ptr.label, end='\t')
    ptr = ptr.next
    while(ptr.label != first.label):
        print(ptr.label, end='\t')
        ptr = ptr.next
    print('\n')


def part_2(cups):
    # rest = list(range(max(cups)+1, 1000_000+1))
    # cups.extend(rest)

    dll = get_dll(cups)

    first, curr_ptr = simulate_move_dll(dll, dll)
    for _ in range(99):
        first, curr_ptr = simulate_move_dll(first, curr_ptr)

    # print(cups)
    # cups.rotate(-cups.index(1))
    # print(cups)
    # return ''.join([str(i) for i in list(cups)[1:]])
    # cups.rotate(-cups.index(1))
    # print(list(cups)[:20])
    # print([str(i) for i in list(cups)[1:3]])


def get_result():
    cups = get_data()

    part_2(cups)

    # part 1
    # tic = time.perf_counter()
    # res1 = part_1(cups)
    # toc = time.perf_counter()
    # print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    # tic = time.perf_counter()
    # res2 = part_2(p1_deck.copy(), p2_deck.copy())
    # toc = time.perf_counter()
    # print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 34664
# 32018
get_result()
