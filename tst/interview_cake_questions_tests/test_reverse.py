import pytest

from src.algorithms.interview_cake_questions.reverse import reverse


def test_example():
    chars = ["a", "b", "c"]
    expected = ["c", "b", "a"]

    assert reverse(chars) == expected


def test_example_2():
    chars = ["a", "b", "c", "d"]
    expected = ["d", "c", "b", "a"]

    assert reverse(chars) == expected


def test_example_3():
    chars = ["a", "b", "c", " ", "f"]
    expected = ["f", " ", "c", "b", "a"]

    assert reverse(chars) == expected
