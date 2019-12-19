import pytest

from src.algorithms.node import Node

from src.algorithms.blind_curated_75_leetcode_questions.maximum_depth_binary_tree import (
    max_depth,
)


def test_example():
    root = Node(3, left=Node(9), right=Node(20, left=Node(15), right=Node(5)))
    expected = 3

    assert max_depth(root) == expected
