import pytest

from src.algorithms.blind_curated_75_leetcode_questions.longest_palindromic_substring import (
    longest_palindrome,
)


def test_example():
    string = "babad"
    expected1 = "aba"
    expected2 = "bab"

    actual = longest_palindrome(string)
    assert actual == expected1 or actual == expected2


def test_only_one_answer():
    string = "vbbd"
    expected = "bb"

    assert longest_palindrome(string) == expected


def test_entire_odd_len_string_is_palindrome():
    string = "racecar"
    expected = "racecar"

    assert longest_palindrome(string) == expected


def test_entire_even_len_string_is_palindrome():
    string = "abba"
    expected = "abba"

    assert longest_palindrome(string) == expected


def test_palindrome_on_left_odd_len():
    string = "bbbad"
    expected = "bbb"

    assert longest_palindrome(string) == expected


def test_palindrome_on_right_len():
    string = "zdsfgddd"
    expected_right = "ddd"

    assert longest_palindrome(string) == expected_right


def test_palindrome_on_left_even_len():
    string = "bbbbad"
    expected = "bbbb"

    assert longest_palindrome(string) == expected


def test_palindrome_on_right_even_len():
    string = "sdsfgdddd"
    expected = "dddd"

    assert longest_palindrome(string) == expected


def test_single_string():
    string = "s"
    expected = "s"

    assert longest_palindrome(string) == expected
