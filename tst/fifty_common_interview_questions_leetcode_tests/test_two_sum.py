import pytest
import hypothesis.strategies as st

from src.algorithms.fifty_common_interview_questions_leetcode_book.two_sum import (
    two_sum,
)
from hypothesis import given


@given(st.lists(st.integers(), max_size=0), st.integers())
def test_empty_list(x, y):
    assert two_sum(x, y) is False


def test_example():
    arr = [2, 7, 11, 15]
    tgt = 9
    actual = two_sum(arr, tgt)

    assert actual is True


def test_empty():
    arr = []
    tgt = 2
    actual = two_sum(arr, tgt)

    assert actual is False


def test_single():
    arr = [1]
    tgt = 2
    actual = two_sum(arr, tgt)

    assert actual is False


def test_duplicate():
    arr = [2, 2, 3]
    tgt = 4
    actual = two_sum(arr, tgt)

    assert actual is True


def test_negative_integers_included():
    arr = [9, -6, -7, 6, 3]
    tgt = -13
    actual = two_sum(arr, tgt)

    assert actual is True


def test_half_target_included():
    arr = [9, 7, 3]
    tgt = 14
    actual = two_sum(arr, tgt)

    assert actual is False


def test_sorted_ascending():
    arr = [x for x in range(10)]
    tgt = 17
    actual = two_sum(arr, tgt)

    assert actual is True


def test_sorted_descending():
    n = [x for x in range(9, -1, -1)]
    k = 3
    actual = two_sum(n, k)

    assert actual is True


def test_only_neg():
    n = [-23434, -2, -4, -16, -5]
    k = -21
    actual = two_sum(n, k)

    assert actual is True


def test_zero_only():
    actual = two_sum([0], -343)

    assert actual is False
