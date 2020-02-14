import pytest
from src.algorithms.blind_curated_75_leetcode_questions.unique_paths import uniquePaths


def test_example():
    base = 3
    height = 2
    expected = 3

    actual = uniquePaths(base, height)

    assert actual == expected


def test_larger_board():
    base = 7
    height = 3
    expected = 28

    actual = uniquePaths(base, height)

    assert actual == expected


def test_square_board_of_2():
    base = 2
    height = 2
    expected = 2

    actual = uniquePaths(base, height)

    assert actual == expected


def test_square_board_of_1():
    base = 1
    height = 1
    expected = 1

    actual = uniquePaths(base, height)

    assert actual == expected
