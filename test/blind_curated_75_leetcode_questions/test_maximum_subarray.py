import pytest
import hypothesis.strategies as st

from src.algorithms.blind_curated_75_leetcode_questions.maximum_subarray import (
    get_largest_sum_subarray,
)
from hypothesis import given


@given(st.lists(st.integers(), max_size=0))
def test_empty_list(n):
    assert get_largest_sum_subarray(n) == 0


def test_negative_numbers_only():
    n = [-43, -1, -5, -2, -6534]
    assert get_largest_sum_subarray(n) == -1


def test_positive_numbers_only():
    n = [1, 56, 767, 44, 32, 3]
    assert get_largest_sum_subarray(n) == sum(n)


def test_pos_neg_numbers():
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert get_largest_sum_subarray(n) == 6


def test_zero_pos_numbers():
    a = [0, 1, 3, 0, 0, 2, 9, 7, 10]
    assert get_largest_sum_subarray(a) == 32
