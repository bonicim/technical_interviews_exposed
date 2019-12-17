import pytest

from src.algorithms.node import Node
from src.algorithms.blind_curated_75_leetcode_questions.merge_two_lists import (
    merge_two_lists,
)


def test_example():
    list1 = Node(1, next=Node(2, next=Node(4)))
    list2 = Node(1, next=Node(3, next=Node(4)))
    expected = Node(
        1,
        next=Node(
            1, next=Node(2, next=Node(2, next=Node(3, next=Node(4, next=Node(4)))))
        ),
    )

    assert merge_two_lists(list1, list2) == expected


def test_list2_is_longer():
    list1 = Node(1, next=Node(2, next=Node(4)))
    list2 = Node(1, next=Node(3, next=Node(4, next=Node(5))))
    expected = Node(
        1,
        next=Node(
            1,
            next=Node(
                2, next=Node(2, next=Node(3, next=Node(4, next=Node(4, next=Node(5)))))
            ),
        ),
    )

    assert merge_two_lists(list1, list2) == expected


def test_list1_is_longer():
    list2 = Node(1, next=Node(2, next=Node(4)))
    list1 = Node(1, next=Node(3, next=Node(4, next=Node(5))))
    expected = Node(
        1,
        next=Node(
            1,
            next=Node(
                2, next=Node(2, next=Node(3, next=Node(4, next=Node(4, next=Node(5)))))
            ),
        ),
    )

    assert merge_two_lists(list1, list2) == expected


def test_list2_is_null():
    list2 = None
    list1 = Node(1, next=Node(3, next=Node(4, next=Node(5))))
    expected = Node(1, next=Node(3, next=Node(4, next=Node(5))))

    assert merge_two_lists(list1, list2) == expected
