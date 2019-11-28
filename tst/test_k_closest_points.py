import pytest

from src.algorithms.k_closest_points_to_origin import get_closest_points


def test_example_1():
    points = [[1, 3], [-2, 2]]
    target = 1
    expected = [[-2, 2]]

    assert get_closest_points(points, target) == expected


def test_example_2():
    points = [[3, 3], [5, -1], [-2, 4]]
    target = 2
    expected = [[3, 3], [-2, 4]]

    assert get_closest_points(points, target) == expected


def test_duplicates_should_return_1():
    points = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]]
    target = 1
    expected = [[1, 1]]

    assert get_closest_points(points, target) == expected
