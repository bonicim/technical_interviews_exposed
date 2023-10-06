import pytest

from src.algorithms.blind_curated_75_leetcode_questions.minimum_window_substring import (
    min_window,
)


def test_example():
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"

    assert min_window(s, t) == expected
