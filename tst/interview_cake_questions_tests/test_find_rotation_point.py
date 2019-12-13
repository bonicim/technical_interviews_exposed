import pytest

from src.algorithms.interview_cake_questions.find_rotation_point import (
    find_rotation_point,
)


def test_example():
    words = [
        "ptolemaic",
        "retrograde",
        "supplant",
        "undulate",
        "xenoepist",
        "asymptote",  # <-- rotates here!
        "babka",
        "banoffee",
        "engender",
        "karpatka",
        "othellolagkage",
    ]
    expected = 5

    assert find_rotation_point(words) == expected
