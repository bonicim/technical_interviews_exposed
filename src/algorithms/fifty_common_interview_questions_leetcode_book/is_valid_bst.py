"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

""" Commentary

The interesting thing about this problem and the solution is that it uses DFS as a strategy to
determine if a tree is a valid BST. Moreover, in order to know if it is a valid BST, we have to initially
set arbitrary lower and upper bounds to determine validity at a node. If the node is valid, then
we need to check the left and right subtree, but with adjusted lower and upper bounds, namely coming from the
parent node. For example, the left child should be greater than the lower bound and less than the current node' value.
For the the right child, the child should be greater than the current node but less than the upper bound.

In both solutions, I purposely stop checking the right side if the left side has already been determined to be
invalid. In this way, I avoid validating both sides. I simply need to know if any side is invalid. If I knew
the left side was invalid, then there is no need to check the right side.

"""


def is_valid_bst(root):
    return recursive_solution(root, float("-inf"), float("inf"))
    # return iterative_top_down_solution(root)


def recursive_solution(node, lower_bound, higher_bound):
    if not node:
        return True
    if node.data <= lower_bound or node.data >= higher_bound:
        return False
    if not recursive_solution(node.left, lower_bound, node.data):
        return False
    if not recursive_solution(node.right, node.data, higher_bound):
        return False
    return True


# this solution uses space of n
#
def iterative_top_down_solution(root):
    node_and_bounds_stack = [(root, -float("inf"), float("inf"))]

    while len(node_and_bounds_stack):
        parent_node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if parent_node.data <= lower_bound or parent_node.data >= upper_bound:
            return False

        # since the node is currently balanced, we need to check the left and right children
        if parent_node.left:
            node_and_bounds_stack.append(
                (parent_node.left, lower_bound, parent_node.data)
            )
        if parent_node.right:
            node_and_bounds_stack.append(
                (parent_node.right, parent_node.data, upper_bound)
            )

    # we only end up here after checking every node to validate that it is a BST
    return True
