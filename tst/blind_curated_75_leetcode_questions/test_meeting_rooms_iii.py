import pytest

from src.algorithms.blind_curated_75_leetcode_questions.meeting_rooms_iii import (
    merge_ranges,
)


def test_example():
    meeting_blocks = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    expected = [(0, 1), (3, 8), (9, 12)]

    assert merge_ranges(meeting_blocks) == expected


def test_meetings_touch():
    meeting_blocks = [(3, 6), (6, 8)]
    expected = [(3, 8)]

    assert merge_ranges(meeting_blocks) == expected


def test_last_meeting_overlaps_current_ends():
    meeting_blocks = [(3, 6), (4, 8)]
    expected = [(3, 8)]

    assert merge_ranges(meeting_blocks) == expected


def test_last_meeting_overlaps_current_completes_before_last_meeting_ends():
    meeting_blocks = [(3, 15), (4, 6)]
    expected = [(3, 15)]

    assert merge_ranges(meeting_blocks) == expected
