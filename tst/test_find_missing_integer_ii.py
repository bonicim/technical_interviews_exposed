import pytest

from src.algorithms.find_missing_integer_ii import find_missing_integer_ii


def test_simple_case_should_return_4():
    nums = [2, 3, 6, 1, 5, 0]
    expected = 4

    assert find_missing_integer_ii(nums) == expected


def test_simple_case_should_return_5():
    nums = [2, 3, 6, 1, 4, 0]
    expected = 5

    assert find_missing_integer_ii(nums) == expected


def test_all_contiguous_should_return_length_of_list():
    nums = [2, 3, 6, 1, 4, 0, 5]
    expected = 7

    assert find_missing_integer_ii(nums) == expected


def test_zero_is_missing_should_0():
    nums = [2, 3, 6, 1, 4, 5]
    expected = 0

    assert find_missing_integer_ii(nums) == expected


def test_single_item_should_return_1():
    nums = [0]
    expected = 1

    assert find_missing_integer_ii(nums) == expected


def test_sorted_list_should_return_4():
    nums = [0, 1, 2, 3]
    expected = 4

    assert find_missing_integer_ii(nums) == expected


def test_sorted_list_descending_should_return_3():
    nums = [5, 4, 2, 1, 0]
    expected = 3

    assert find_missing_integer_ii(nums) == expected
