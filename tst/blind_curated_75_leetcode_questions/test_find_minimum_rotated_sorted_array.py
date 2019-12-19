import pytest

from src.algorithms.blind_curated_75_leetcode_questions.find_minimum_rotated_sorted_array import (
    find_min,
)


def test_example():
    nums = [3, 4, 5, 1, 2]
    expected = 1

    assert find_min(nums) == expected


def test_single_item():
    nums = [1]
    expected = 1

    assert find_min(nums) == expected


def test_not_rotated():
    nums = [0, 1, 2, 3]
    expected = 0

    assert find_min(nums) == expected


def test_two_items():
    nums = [434, 41]
    expected = 41

    assert find_min(nums) == expected
