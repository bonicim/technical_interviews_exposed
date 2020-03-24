import pytest

from src.algorithms.pramp_questions.busiest_time_in_mall import find_busiest_period


def test_example():
    data = [
        [1487799425, 14, 1],
        [1487799425, 4, 0],
        [1487799425, 2, 0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1, 0],
        [1487901211, 7, 1],
        [1487901211, 7, 0],
    ]

    expected = 1487800378

    actual = find_busiest_period(data)

    assert actual == expected
