import pytest

from src.algorithms.recursion_questions.combination_sum import combination_sum


def test_example():
    choices = [2, 3, 6, 7]
    tgt = 7
    expected = [[2, 2, 3], [7]]

    actual = combination_sum(choices, tgt)

    assert actual == expected


def test_example2():
    choices = [2, 3, 5]
    tgt = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    actual = combination_sum(choices, tgt)

    assert actual == expected


def test_example3_sorted_descending():
    choices = [7, 6, 3, 2]
    tgt = 7
    expected = [[7], [2, 2, 3]]

    actual = combination_sum(choices, tgt)

    assert actual == expected
