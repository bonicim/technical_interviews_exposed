import pytest
from src.algorithms.longest_common_substring import lcs


def test_example_should_return_3():
    text1 = "fish"
    text2 = "hish"
    expected = 3

    assert lcs(text1, text2) == expected


def test_example_should_return_2():
    text1 = "hish"
    text2 = "vista"
    expected = 2

    assert lcs(text1, text2) == expected
