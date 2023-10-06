import pytest

from src.algorithms.blind_curated_75_leetcode_questions.lowest_common_ancestor import (
    recursive_solution,
)
from src.algorithms.node import Node


def test_example():
    root = Node(2, left=Node(1), right=Node(3))
    node1 = Node(1)
    node2 = Node(3)
    expected = 2

    assert recursive_solution(root, node1, node2) == expected


def test_ancestor_on_left():
    root = Node(2, left=Node(0), right=Node(4, left=Node(3), right=Node(5)))
    node1 = Node(2)
    node2 = Node(4)
    expected = 2

    assert recursive_solution(root, node1, node2) == expected


def test_ancestor_on_right():
    root = Node(2, left=Node(0), right=Node(4, left=Node(3), right=Node(5)))
    node1 = Node(0)
    node2 = Node(2)
    expected = 2

    assert recursive_solution(root, node1, node2) == expected
