from src.algorithms.node import Node

# Given a list of integers as the leafs of a binary tree, create a balanced binary tree, in which
# the sum of a node's children will equal the node's value. 
# Return the root of the binary tree.
#
# Print the binary tree as the following:
# For example, given the list [1, 2, 3, 3, 4, 10]
# Print the following balanced binary tree
#                  [23,
#                  9, 14,
#               3, 6, 14, 0
#          1, 2, 3, 3, 4, 10, 0, 0]
def create_balanced_binary_tree():
    list_first_line = list(input().split())
    list_first_line = list(map(int, list_first_line))
    list_first_line.sort()

    known_leaves = len(list_first_line)
    total_leaf_size = 2**((len(list_first_line)-1).bit_length())

    tree = []
    tree.extend([0]*(total_leaf_size-1))
    tree.extend(list_first_line)
    tree.extend([0]*(total_leaf_size-known_leaves))

    start_at = total_leaf_size-2

    while start_at>= 0:
        tree[start_at] = tree[2*start_at+1] + tree[2*start_at+2]
        start_at -= 1

    print(tree)