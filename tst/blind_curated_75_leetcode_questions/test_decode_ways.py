import pytest
from src.algorithms.blind_curated_75_leetcode_questions.decode_ways import decode_ways


def test_example():
    s = "226"
    expected = 3

    assert decode_ways(s) == expected


def test_leading_zero_string():
    s = "054654654654"
    expected = 0

    assert decode_ways(s) == expected
