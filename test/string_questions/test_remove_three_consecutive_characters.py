import pytest
from src.algorithms.string_questions.remove_three_consecutive_characters import (
    remove_three_consecutive_characters,
)


def test_example():
    word = "baaaaa"
    expected = 1

    actual = remove_three_consecutive_characters(word)

    assert actual == expected


def test_should_return_2():
    word = "baaabbaabbba"
    expected = 2

    actual = remove_three_consecutive_characters(word)

    assert actual == expected


def test_no_changes_needed():
    word = "baabab"
    expected = 0

    actual = remove_three_consecutive_characters(word)

    assert actual == expected


def test_all_same_letters():
    word = "aaaaaaaaa"
    expected = 3

    actual = remove_three_consecutive_characters(word)

    assert actual == expected


def test_empty_should_return_0():
    word = ""
    expected = 0

    actual = remove_three_consecutive_characters(word)

    assert actual == expected


def test_single_char_should_return_0():
    word = "a"
    expected = 0

    actual = remove_three_consecutive_characters(word)

    assert actual == expected
