import pytest

from src.algorithms.pramp_questions.shortest_unique_substring import (
    get_shortest_unique_substring,
)


def test_example():
    arr = ["x", "y", "z"]
    str_a = "xyyzyzyx"
    expected = "zyx"

    actual = get_shortest_unique_substring(arr, str_a)

    assert actual == expected
