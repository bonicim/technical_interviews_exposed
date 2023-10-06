from src.algorithms.node import Node

# Given the root of a binary search tree and two of its children, find the nearest ancestor
# Assume that all inputs will never be null or empty and that all node values are unique


def get_nearest_ancestor(root, val1, val2):
    while root:
        if val1 > root.data and val2 > root.data:
            root = root.right
        elif val1 < root.data and val2 < root.data:
            root = root.left
        else:
            return root
