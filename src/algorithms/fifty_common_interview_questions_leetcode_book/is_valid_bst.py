"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


def is_valid_bst(root):
    # return recursive_solution(root, float("-inf"), float("inf"))
    return iterative_solution(root)


def recursive_solution(root, lower_bound, higher_bound):
    if not root:
        return True
    if root.data <= lower_bound or root.data >= higher_bound:
        return False
    return recursive_solution(root.left, lower_bound, root.data) and recursive_solution(
        root.right, root.data, higher_bound
    )


def iterative_solution(root):
    node_and_bounds_stack = [(root, -float("inf"), float("inf"))]

    while len(node_and_bounds_stack):
        parent_node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if parent_node.data <= lower_bound or parent_node.data >= upper_bound:
            return False

        if parent_node.left:
            node_and_bounds_stack.append(
                (parent_node.left, lower_bound, parent_node.data)
            )
        if parent_node.right:
            node_and_bounds_stack.append(
                (parent_node.right, parent_node.data, upper_bound)
            )

    return True
