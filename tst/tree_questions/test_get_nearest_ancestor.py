import pytest
from src.algorithms.tree_questions.get_nearest_ancestor import get_nearest_ancestor
from src.algorithms.node import Node


def test_typical_case():
    assert get_nearest_ancestor(root, 10, 30) == Node(20)


def test_left_branch():
    assert get_nearest_ancestor(root, 5, 19) == Node(10)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(19)
root.right.left = Node(25)
root.right.right = Node(41)
