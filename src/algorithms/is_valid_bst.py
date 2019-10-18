"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


def is_valid_bst(root):
    return valid_bst_v1(root, float("-inf"), float("inf"))
    # return valid_bst_v2(root, None)


# recursive solution
def valid_bst_v1(root, low_data, high_data):
    if not root:
        return True
    elif low_data >= root.data or high_data <= root.data:
        return False
    else:
        return valid_bst_v1(root.left, low_data, root.data) and valid_bst_v1(
            root.right, root.data, high_data
        )
