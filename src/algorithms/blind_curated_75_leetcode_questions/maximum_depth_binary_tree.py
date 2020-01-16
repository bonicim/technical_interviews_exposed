"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

"""Commentary

This is a classic tree searching question that tests if you know DFS and know how to code it up quickly. The algorithm
simply is to get the height of the left and right side. Compare them. And choose the bigger height. Very simple.

The key to this is recursion. You want to use the call stack (not a stack data structure, although you can) to hold your
recursive calls. You need to know what is the base case (aka stopping point). And you need to know how to use accumulators implicitly
to get the total height of each side.

"""


def max_depth(root):
    if not root:
        return 0

    left_depth = 1 + max_depth(root.left)
    right_depth = 1 + max_depth(root.right)

    return max(left_depth, right_depth)
