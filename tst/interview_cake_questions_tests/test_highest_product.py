import pytest

from src.algorithms.interview_cake_questions.highest_product import three_product


def test_example():
    nums = [-10, -10, 1, 3, 2]
    expected = 300

    assert three_product(nums) == expected


def test_all_positives():
    nums = [5, 3, 2, 10, 5, 7]
    expected = 350

    assert three_product(nums) == expected


def test_all_negatives():
    nums = [-2, -4, -1, -7, -3]
    expected = -6

    assert three_product(nums) == expected


def test_all_duplicates():
    nums = [9, 9, 9, 9, 9, 9]
    expected = 729

    assert three_product(nums) == expected
