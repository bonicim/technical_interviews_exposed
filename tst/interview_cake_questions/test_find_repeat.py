import pytest

from src.algorithms.interview_cake_questions.find_repeat import find_repeat


def test_example():
    nums = [1, 4, 2, 3, 6, 5, 4]
    expected = 4

    assert find_repeat(nums) == expected


def test_more_one_duplicate_should_return_5():
    nums = [5, 5, 5, 3, 4, 6, 6]
    expected = 5

    assert find_repeat(nums) == expected
