"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""


def find_max_sum_binary_tree(root):
    def find_max(node):
        nonlocal max_sum
        if not node:
            return 0

        left_max = find_max(node.left)
        right_max = find_max(node.right)
        sum_at_node_as_starting_point = node.data + left_max + right_max
        max_sum = max(max_sum, sum_at_node_as_starting_point)

        max_at_node = node.data + max(left_max, right_max)
        if max_at_node > 0:
            return max_at_node
        return 0

    max_sum = float("-inf")
    find_max(root)
    return max_sum
