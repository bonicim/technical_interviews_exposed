import pytest
from src.algorithms.pramp_questions.meeting_planner import meeting_planner


def test_no_overlap():
    a = [[1, 10], [15, 20]]
    b = [[100, 200]]
    dur = 3

    pass_test(meeting_planner(a, b, dur), [])


def test_subsume_overlap():
    a = [[1, 10], [15, 20]]
    b = [[4, 7]]
    dur = 3
    pass_test(meeting_planner(a, b, dur), [4, 7])


def test_left_overlap():
    a = [[1, 10], [15, 20]]
    b = [[12, 18]]
    dur = 3

    pass_test(meeting_planner(a, b, dur), [15, 18])


def test_right_overlap():
    a = [[1, 10], [15, 20]]
    b = [[16, 4738]]
    dur = 3

    pass_test(meeting_planner(a, b, dur), [16, 19])


def pass_test(actual, expected):
    assert actual == expected
