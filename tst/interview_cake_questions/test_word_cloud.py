import pytest

from src.algorithms.interview_cake_questions.word_cloud import word_cloud


def test_example():
    word = "After beating the eggs, Dana read the next step:"
    expected = {
        "After": 1,
        "beating": 1,
        "the": 2,
        "eggs": 1,
        "Dana": 1,
        "read": 1,
        "next": 1,
        "step": 1,
    }

    assert word_cloud(word) == expected


def test_checks_all_branches():
    word = "The repeat repeat Repeat Cliff cliff"
    expected = {"The": 1, "repeat": 3, "cliff": 2}

    assert word_cloud(word) == expected
