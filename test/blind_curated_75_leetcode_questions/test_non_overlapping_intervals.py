import pytest

from src.algorithms.blind_curated_75_leetcode_questions.non_overlapping_intervals import (
    erase_overlap_intervals,
)


def test_example():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expected = 1

    assert erase_overlap_intervals(intervals) == expected


def test_duplicates():
    intervals = [[1, 2], [1, 2], [1, 2]]
    expected = 2

    assert erase_overlap_intervals(intervals) == expected


def test_no_overlaps():
    intervals = [[1, 2], [2, 3]]
    expected = 0

    assert erase_overlap_intervals(intervals) == expected


def test_no_overlap_within_larger_inteval():
    intervals = [[3, 14], [4, 7], [8, 10]]
    expected = 1

    assert erase_overlap_intervals(intervals) == expected


def test_no_overlap_within_larger_inteval_but_outside_end_time():
    intervals = [[3, 14], [4, 17], [15, 17]]
    expected = 1

    assert erase_overlap_intervals(intervals) == expected
