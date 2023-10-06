import pytest

from src.algorithms.blind_curated_75_leetcode_questions.search_rotated_sorted_array import (
    search,
)


def test_example():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    expected = 4

    assert search(nums, target) == expected


def test_target_not_found():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1

    assert search(nums, target) == expected


def test_not_rotated_list():
    nums = [4, 5, 6, 7, 434, 565, 5555, 55555]
    target = 7
    expected = 3

    assert search(nums, target) == expected


def test_not_rotated_list_target_is_first():
    nums = [4, 5, 6, 7, 434, 565, 5555, 55555]
    target = 4
    expected = 0

    assert search(nums, target) == expected


def test_empty_list():
    nums = []
    target = 5
    expected = -1

    assert search(nums, target) == expected


def test_single_item():
    nums = [1]
    target = 0
    expected = -1

    assert search(nums, target) == expected
