import pytest

from src.algorithms.search_questions.count_battleships import count_battleships


def test_two_battleships():
    ocean_map = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]

    assert count_battleships(ocean_map) == 2


def test_one_battleship():
    ocean_map = [
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]

    assert count_battleships(ocean_map) == 1


def test_zero_battleship():
    ocean_map = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]

    assert count_battleships(ocean_map) == 0


def test_four_diagonal_battleships():
    ocean_map = [
        ["X", ".", ".", "."],
        [".", "X", ".", "."],
        [".", ".", "X", "."],
        [".", ".", ".", "X"],
    ]

    assert count_battleships(ocean_map) == 4
