import pytest

from src.algorithms.blind_curated_75_leetcode_questions.meeting_rooms_ii import (
    min_meeting_rooms,
)


def test_example():
    intervals = [[0, 30], [5, 10], [15, 20]]
    expected = 2

    assert min_meeting_rooms(intervals) == expected


def test_unsorted_no_overlapping_meetings():
    intervals = [[50, 9695], [5, 10], [15, 20]]
    expected = 1

    assert min_meeting_rooms(intervals) == expected


def test_unsorted_one_meeting():
    intervals = [[50, 9695]]
    expected = 1

    assert min_meeting_rooms(intervals) == expected


def test_unsorted_all_overlap_need_max_rooms():
    intervals = [[2, 15], [5, 20], [3, 30], [13, 45454]]
    expected = 4

    assert min_meeting_rooms(intervals) == expected


def test_unsorted_all_two_meetings_same_time():
    intervals = [[50, 96], [96, 200], [96, 200], [96, 200]]
    expected = 3

    assert min_meeting_rooms(intervals) == expected


def test_unsorted_all_meetings_adjacent_but_not_on_each_other():
    intervals = [[3, 5], [1, 2], [6, 15], [16, 20]]
    expected = 1

    assert min_meeting_rooms(intervals) == expected
