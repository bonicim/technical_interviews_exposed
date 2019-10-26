import pytest

from src.algorithms.get_index_equals_value import get_index_equals_value


def test_get_index_sorted_start_at_0_should_return_0():
    arr = [0, 1, 2, 3]

    assert get_index_equals_value(arr) == 0


def test_simple_case_should_return_negative_index():
    arr = [1, 2, 3]
    assert get_index_equals_value(arr) == -1


def test_match_is_at_end_should_return_index():
    arr = [-789787, -51, 0, 3]

    assert get_index_equals_value(arr) == 3


def test_empty_list():
    arr = []

    assert get_index_equals_value(arr) == -1


def test_index_in_middle():
    arr = [-54645, -55, -1, 3, 78, 898, 6361487]

    assert get_index_equals_value(arr) == 3


def test_single_list_with_zero_should_return_0():
    assert get_index_equals_value([0]) == 0


def test_single_list_with_non_zero_should_return_negative_1():
    assert get_index_equals_value([42]) == -1
