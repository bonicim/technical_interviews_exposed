"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

""" Commentary
When we hear Binary Search Tree, we should immediately think how we can use the properties of a BST
to solve the question.

In this case, we need to find the lowest common ancestor for any two nodes in a tree. So what does that really mean?
It means that the lowest common ancestor is the node that is immediately above two of the child nodes. But there is a catch.
Just because two nodes less or greater than the current node, it doesn't mean that we found the lowest common ancestor.
The ancestor is found when the two nodes are split, i.e. one node is less than the current node we're on and the other is
greater than. If we are at that point, then we have found the lowest common ancestor.
"""


def lowest_common_ancestor(root, node1, node2):
    # return iterative_solution(root, node1, node2)
    return recursive_solution(root, node1, node2)


def recursive_solution(root, node1, node2):
    parent_data = root.data
    node1_data = node1.data
    node2_data = node2.data

    if node1_data > parent_data and node2_data > parent_data:
        return recursive_solution(root.right, node1, node2)
    elif node1_data < parent_data and node2_data < parent_data:
        return recursive_solution(root.left, node1, node2)
    # This is where the two nodes are in different subtrees, thus they share the same parent
    return root.data


def iterative_solution(root, node1, node2):
    node1_data = node1.data
    node2_data = node2.data
    current = root

    while current:
        current_data = current.data
        if node1_data > current_data and node2_data > current_data:
            current = current.right
        elif node1_data < current_data and node2_data < current_data:
            current = current.right
        # This is where the two nodes are in different subtrees, thus they share the same parent
        return current.data
