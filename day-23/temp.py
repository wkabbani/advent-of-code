from collections import deque


class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


my_input = [int(i) for i in "362981754"]


def part2():
    my_nodes = {}

    last_node = None
    for i in my_input:
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node

        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node

        last_node = curr_node
    for i in range(len(my_input)+1, 1_000_001):
        curr_node = LinkedListNode(i)
        my_nodes[i] = curr_node
        if last_node is not None:
            last_node.right = curr_node
            curr_node.left = last_node
        last_node = curr_node

    # Complete the circle
    ptr = my_nodes[my_input[0]]
    last_node.right = ptr
    ptr.left = last_node

    ptr = my_nodes[my_input[0]]
    for i in range(10000000):
        p_val = ptr.item

        cup1 = ptr.right
        cup2 = cup1.right
        cup3 = cup2.right

        ptr.right = cup3.right
        ptr.right.left = ptr

        d_val = p_val - 1 or 1000000
        while d_val in (cup1.item, cup2.item, cup3.item):
            d_val = d_val - 1 or 1000000

        d_node = my_nodes[d_val]

        cup3.right = d_node.right
        cup3.right.left = cup3
        d_node.right = cup1
        cup1.left = d_node

        ptr = ptr.right

    while ptr.item != 1:
        ptr = ptr.right

    return ptr.right.item * ptr.right.right.item


print(f"Part 2 solution: {part2()}")
