import pytest

from src.algorithms.get_blob_boundaries import get_blob_boundaries


def test_typical_case():
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]]

    assert get_blob_boundaries(matrix) == {"Top": 1, "Left": 2, "Bottom": 1, "Right": 4}


def test_10_by_10_matrix():
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    assert get_blob_boundaries(matrix) == {"Top": 1, "Left": 2, "Bottom": 7, "Right": 6}


def test_blob_is_the_entire_matrix():
    matrix = [[1 for _ in range(10)] for _ in range(10)]

    assert get_blob_boundaries(matrix) == {"Top": 0, "Left": 0, "Bottom": 9, "Right": 9}
