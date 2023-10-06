import pytest
from src.algorithms.fifty_common_interview_questions_leetcode_book.reverse_word import (
    reverse_word,
)


def test_example():
    word = "the sky is blue"
    expected = "blue is sky the"

    assert reverse_word(word) == expected


def test_leading_trailing_spaces_removed():
    word = "  hello world!  "
    expected = "world! hello"

    assert reverse_word(word) == expected


def test_reduce_in_between_spaces_to_one():
    word = "a good   example"
    expected = "example good a"

    assert reverse_word(word) == expected
