import pytest

from src.algorithms.fifty_common_interview_questions_leetcode_book.two_sum_sorted_array import (
    two_sum_sorted_array,
)


def test_simple_case_should_return_1_2_indexes():
    arr = sorted([2, 7, 11, 15])
    tgt = 9

    assert two_sum_sorted_array(arr, tgt) == (1, 2)


def test_simple_case_should_return_3_5_indexes():
    arr = sorted([5, 6, 7, 10, 11, 13])
    tgt = 23

    assert two_sum_sorted_array(arr, tgt) == (4, 6)


def test_indexes_are_in_far_left_should_return_0_1_indexes():
    arr = sorted([5, 6, 7, 10, 11, 13])
    tgt = 11

    assert two_sum_sorted_array(arr, tgt) == (1, 2)


def test_indexes_are_in_far_right_should_return_4_5_indexes():
    arr = sorted([5, 6, 7, 10, 11, 13])
    tgt = 24

    assert two_sum_sorted_array(arr, tgt) == (5, 6)


def test_odd_list_indexes_are_in_far_right_should_return_3_4_indexes():
    arr = sorted([5, 6, 7, 10, 11])
    tgt = 21

    assert two_sum_sorted_array(arr, tgt) == (4, 5)


def test_odd_list_indexes_are_in_far_left_should_return_0_1_indexes():
    arr = sorted([5, 6, 7, 10, 11])
    tgt = 11

    assert two_sum_sorted_array(arr, tgt) == (1, 2)


def test_odd_list_indexes_are_in_middle_should_return_2_3_indexes():
    arr = sorted([0, 2, 7, 10, 11])
    tgt = 17

    assert two_sum_sorted_array(arr, tgt) == (3, 4)


def test_duplicates_equals_target_odd_list_return_4_5_indexes():
    arr = sorted([1, 2, 3, 4, 4, 9, 99, 765, 965433])
    tgt = 8

    assert two_sum_sorted_array(arr, tgt) == (4, 5)


def test_duplicates_equals_target_even_list_return_4_5_indexes():
    arr = sorted([1, 2, 3, 4, 4, 9, 99, 767])
    tgt = 8

    assert two_sum_sorted_array(arr, tgt) == (4, 5)
