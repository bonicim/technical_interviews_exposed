from src.algorithms.binary_tree_inorder_traversal import inorder_traversal
from src.algorithms.node import Node


def test_degenerate_binary_tree():
    """
    a binary tree in which each parent node only has one child, essentially behaving like a linked list
        1
         \
          2
         /
        3
    """
    node3 = Node(3)
    node2 = Node(2, left=node3)
    root = Node(1, right=node2)

    assert inorder_traversal(root) == [1, 3, 2]


def test_null_tree():
    assert inorder_traversal(None) == []


def test_single_tree():
    assert inorder_traversal(Node(2)) == [2]


def test_complete_binary_tree():
    """
    a complete binary tree is a tree in which every level, except possibly the last, is completely filled
    and all nodes in the last level are as far left as possible
        1
       /  \
      2   5
     /  \
    3   4

    """
    arr = [1, 2, 5, 3, 4]
    root = build_complete_binary_tree(arr, None, 0, 5)

    assert inorder_traversal(root) == [3, 2, 4, 1, 5]


def test_full_binary_tree():
    """
    a full binary tree is a tree in which every node has 0 or 2 children

        5
       / \
      42  10
     /  \
    6   10
       /  \
      3    4
    """
    node10 = Node(10, left=Node(3), right=Node(4))
    node42 = Node(42, left=Node(6), right=node10)
    root = Node(5, left=node42, right=Node(10))

    assert inorder_traversal(root) == [6, 42, 3, 10, 4, 5, 10]


def test_perfect_binary_tree():
    """
    a perfect binary tree is a tree in which all nodes have two children and all leaves are on the same level; a perfect tree is a complete tree.
    The number of nodes is equal to 2^N -1, where N is the height of the tree with the root counting as part of the height. Thus, the example below shows a height of 3.
          1
       /     \
      2       3
     /  \    / \
    4    5  6   7
    """
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = build_complete_binary_tree(arr, None, 0, 7)

    assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]


def test_balanced_binary_tree():
    """
    a balanced binary tree is a tree in which the left and right subtrees of every node differ in height by no more than 1

        1
       / \
      2   5
           \
             6
    """
    node5 = Node(5, right=Node(6))
    root = Node(1, left=Node(2), right=node5)

    assert inorder_traversal(root) == [2, 1, 5, 6]


def build_complete_binary_tree(arr, root, index, node_count):
    if index < node_count:
        root = Node(arr[index])

        root.left = build_complete_binary_tree(
            arr, root.left, 2 * index + 1, node_count
        )
        root.right = build_complete_binary_tree(
            arr, root.right, 2 * index + 2, node_count
        )

    return root


def convert_complete_binary_tree_to_list(root):
    result = []
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)

    return result
