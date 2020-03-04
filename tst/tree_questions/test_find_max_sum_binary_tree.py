import pytest

from src.algorithms.node import Node
from src.algorithms.tree_questions.find_max_sum_binary_tree import (
    find_max_sum_binary_tree,
)


def test_basic_case():
    node2leaf = Node(2)
    node3leaf = Node(3)
    node2 = Node(2, left=node2leaf, right=node3leaf)
    node4 = Node(4)
    root = Node(1, left=node2, right=node4)

    assert find_max_sum_binary_tree(root) == 10


def test_negative_nums():
    nodeneg1 = Node(-1)
    node4 = Node(4)
    node2 = Node(2, left=nodeneg1, right=node4)
    node3 = Node(3)
    root = Node(-5, left=node2, right=node3)

    assert find_max_sum_binary_tree(root) == 6
