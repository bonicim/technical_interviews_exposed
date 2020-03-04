import pytest

from src.algorithms.interview_cake_questions.has_palindrome import has_palindrome


def test_odd_length_non_palindrome_word_should_be_true():
    string = "ivicc"

    assert has_palindrome(string) is True


def test_odd_length_non_palindrome_word_should_be_false():
    string = "livc"

    assert has_palindrome(string) is False
