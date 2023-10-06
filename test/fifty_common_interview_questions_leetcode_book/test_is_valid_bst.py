import pytest

from src.algorithms.fifty_common_interview_questions_leetcode_book.is_valid_bst import (
    is_valid_bst,
)
from src.algorithms.node import Node


def test_simplest_valid_bst():
    root = Node(2, left=Node(1), right=Node(3))

    assert is_valid_bst(root) is True


def test_non_valid_bst():
    node3 = Node(3)
    node6 = Node(6)
    node4 = Node(4, left=node3, right=node6)
    root = Node(5, left=Node(1), right=node4)

    assert is_valid_bst(root) is False


def test_same_value_nodes_should_not_be_valid_bst():
    root = Node(1, left=Node(1), right=Node(1))

    assert is_valid_bst(root) is False
