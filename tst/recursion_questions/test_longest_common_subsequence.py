import pytest

from src.algorithms.recursion_questions.longest_common_subsequence import lcm


def test_example_should_return_3():
    text1 = "abcde"
    text2 = "ace"
    expected = 3

    assert lcm(text1, text2) == expected


def test_example_should_return_0():
    text1 = "abc"
    text2 = "def"
    expected = 0

    assert lcm(text1, text2) == expected
