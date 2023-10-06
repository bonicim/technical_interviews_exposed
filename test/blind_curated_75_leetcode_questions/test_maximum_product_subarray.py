import pytest

from src.algorithms.blind_curated_75_leetcode_questions.maximum_product_subarray import (
    product,
)


def test_example():
    nums = [2, 3, -2, 4]
    expected = 6

    assert product(nums) == expected


def test_single_product():
    nums = [-1, 0, -2]
    expected = 0

    assert product(nums) == expected


def test_all_negatives_even_length():
    nums = [-1, -2, -5, -2]
    expected = 20

    assert product(nums) == expected


def test_all_negatives_odd_length():
    nums = [-1, -2, -5, -2, -10]
    expected = 200

    assert product(nums) == expected


def test_two_big_negatives_at_end():
    nums = [1, 2, 5, -2, -100, -42]
    expected = 4200

    assert product(nums) == expected
