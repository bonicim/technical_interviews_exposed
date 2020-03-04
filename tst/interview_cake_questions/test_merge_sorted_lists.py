import pytest

from src.algorithms.interview_cake_questions.merge_sorted_lists import (
    merge_sorted_lists,
)


def test_example():
    list1 = [3, 4, 6, 10, 11, 15]
    list2 = [1, 5, 8, 12, 14, 19]
    expected = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    assert merge_sorted_lists(list1, list2) == expected


def test_example2():
    list1 = [-2, 0, 2]
    list2 = [-1, 1, 4]
    expected = [-2, -1, 0, 1, 2, 4]

    assert merge_sorted_lists(list1, list2) == expected


def test_example_duplicates():
    list1 = [-2, 0, 1]
    list2 = [-1, 0, 4]
    expected = [-2, -1, 0, 0, 1, 4]

    assert merge_sorted_lists(list1, list2) == expected


def test_example_longer_list():
    list1 = [-2, 1, 3, 5, 6, 7]
    list2 = [-1, 0, 4]
    expected = [-2, -1, 0, 1, 3, 4, 5, 6, 7]

    assert merge_sorted_lists(list1, list2) == expected
