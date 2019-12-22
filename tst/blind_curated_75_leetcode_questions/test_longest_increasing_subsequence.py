import pytest

from src.algorithms.blind_curated_75_leetcode_questions.longest_increasing_subsequence import (
    longest_increasing_subsequence,
)


def test_example():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected = 4

    assert longest_increasing_subsequence(nums) == expected


def test_all_decreasing_return_1():
    nums = [10, 9, 7, 4, 2]
    expected = 1

    assert longest_increasing_subsequence(nums) == expected


def test_all_increasing_return_5():
    nums = [5, 7, 45, 456, 89654]
    expected = 5

    assert longest_increasing_subsequence(nums) == expected


def test_single_item():
    nums = [5]
    expected = 1

    assert longest_increasing_subsequence(nums) == expected


def test_empty_list():
    nums = []
    expected = 0

    assert longest_increasing_subsequence(nums) == expected


def test_duplicates():
    nums = [3, 4, 1, 5, 5, 5]
    expected = 3

    assert longest_increasing_subsequence(nums) == expected


def test_all_duplicates():
    nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    expected = 1

    assert longest_increasing_subsequence(nums) == expected
