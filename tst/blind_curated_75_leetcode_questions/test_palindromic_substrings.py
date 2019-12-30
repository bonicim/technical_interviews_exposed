import pytest

from src.algorithms.blind_curated_75_leetcode_questions.palindromic_substrings import (
    count_palindromic_substrings,
)


def test_example():

    string = "abc"
    expected = 3

    assert count_palindromic_substrings(string) == expected


def test_all_same_letters():

    string = "aaa"
    expected = 6

    assert count_palindromic_substrings(string) == expected


def test_whole_word_is_palindrome_only():

    string = "racecar"
    expected = 10

    assert count_palindromic_substrings(string) == expected
