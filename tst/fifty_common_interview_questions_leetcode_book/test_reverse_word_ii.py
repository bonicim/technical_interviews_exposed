import pytest
from src.algorithms.fifty_common_interview_questions_leetcode_book.reverse_word_ii import (
    reverse_word_ii,
)


def test_example():
    word = "the sky is blue"
    word = [x for x in word]
    expected = [
        "b",
        "l",
        "u",
        "e",
        " ",
        "i",
        "s",
        " ",
        "s",
        "k",
        "y",
        " ",
        "t",
        "h",
        "e",
    ]

    assert reverse_word_ii(word) == expected


def test_punctuation():
    word = "hello world!"
    word = [x for x in word]
    expected = ["w", "o", "r", "l", "d", "!", " ", "h", "e", "l", "l", "o"]

    assert reverse_word_ii(word) == expected
