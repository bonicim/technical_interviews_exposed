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

    new_head = Node(5)
    new_temp = new_head
    for i in range(4, 0, -1):
        new_temp.next = Node(i)
        new_temp = new_temp.next

    assert reverse_linked_list(head) == new_head
