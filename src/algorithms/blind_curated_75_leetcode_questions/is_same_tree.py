"""Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

"""

""" Commentary

This problem tests your ability to traverse a binary tree, specifically inorder, postorder, preorder traversals, which
are common. The recursive approach is quite intuitive and descriptive of what it does; the elegance stems from
the use of recursion and a declarative-style. Moreover, the traversal is a DFS-like traversal, searching the farthest left-side, then moves
to the right. The key to being efficient is to stop the search once you have found a node that is not
identical. There is no need to search the right subtree if the left subtree is not identitcal. The code is
refactored to reflect that optimization.


The iterative approach is more procedural and requires explicit data structures and a while loop and a helper function.
"""


def is_same_tree(p, q):
    # both null
    if not p and not q:
        return True
    # one is null
    if not p or not q:
        return False

    # check current node
    if p.val != q.val:
        return False
    # check left side
    if not is_same_tree(p.left, q.left):
        return False
    # check right side
    if not is_same_tree(p.right, q.right):
        return False

    return True


def is_same_tree_iterative(p, q):
    def is_same_node(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True

    nodes_to_visit = []
    nodes_to_visit.append((p, q))

    while nodes_to_visit:
        node1, node2 = nodes_to_visit.pop(0)
        if not is_same_node(node1, node2):
            return False

        if node1:
            nodes_to_visit.append((node1.left, node2.left))
            nodes_to_visit.append((node1.right, node2.right))

    return True
