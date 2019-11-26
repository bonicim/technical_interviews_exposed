import pytest

from src.algorithms.node import Node
from src.algorithms.fifty_common_interview_questions_leetcode_book.is_balanced import (
    is_balanced,
)


def test_simple_case_should_be_true():
    root = Node(3)
    root_left = Node(9)
    root_right = Node(20, left=Node(15), right=Node(7))
    root.left = root_left
    root.right = root_right

    assert is_balanced(root) is True


def test_simple_case_should_be_false():
    root = Node(1)

    root_right = Node(2)

    root_left = Node(2)
    root_left.right = Node(3)
    root_lower_left = Node(3, left=Node(4), right=Node(4))
    root_left.left = root_lower_left

    root.left = root_left
    root.right = root_right

    assert is_balanced(root) is False


def test_single_node_should_be_true():
    assert is_balanced(Node(2)) is True


def test_null_case_should_be_true():
    assert is_balanced(None) is True


def test_unbalanced_at_right_child():
    root = Node(1)

    root_left = Node(2, left=Node(3), right=Node(4))
    root.left = root_left

    root_right = Node(5)
    root_right_right = Node(6, left=Node(7))
    root_right.right = root_right_right
    root.right = root_right

    assert is_balanced(root) is False
