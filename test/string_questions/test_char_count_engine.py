import pytest

from src.algorithms.string_questions.char_count_engine import char_count_engine


def test_example():
    word = "tree"
    expected1 = "eert"
    expected2 = "eetr"

    actual = char_count_engine(word)

    assert actual == expected1 or actual == expected2


def test_capital_letters():
    word = "Aabb"
    expected1 = "bbAa"
    expected2 = "bbaA"

    actual = char_count_engine(word)

    assert actual == expected1 or actual == expected2
