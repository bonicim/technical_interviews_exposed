import pytest

from src.algorithms.blind_curated_75_leetcode_questions.product_of_array_except_self import (
    product_except_self,
)


def test_example():
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]

    assert product_except_self(nums) == expected


def test_unsorted():
    nums = [1, 7, 3, 4]
    expected = [84, 12, 28, 21]

    assert product_except_self(nums) == expected


def test_only_2_integers():
    nums = [8, 3]
    expected = [3, 8]

    assert product_except_self(nums) == expected


def test_negative_ints():
    nums = [2, 3, -3, 4]
    expected = [-36, -24, 24, -18]

    assert product_except_self(nums) == expected
