import pytest

from src.algorithms.node import Node

from src.algorithms.blind_curated_75_leetcode_questions.reverse_linked_list import (
    reverse_linked_list,
)


def test_example():
    head = Node(1)
    temp = head
    for i in range(2, 6):
        temp.next = Node(i)
        temp = temp.next

    expected = Node(5)
    new_temp = expected
    for i in range(4, 0, -1):
        new_temp.next = Node(i)
        new_temp = new_temp.next

    actual = reverse_linked_list(head)

    assert actual == expected
    assert has_cycle(actual) is True


def test_two_items():
    head = Node(1, next=Node(2))
    expected = Node(2, next=Node(1))
    actual = reverse_linked_list(head)

    assert actual == expected
    assert has_cycle(actual) is True


def has_cycle(actual):
    prev = None
    while actual:
        prev = actual
        actual = actual.next

    return prev.next is None
