import pytest

from src.algorithms.blind_curated_75_leetcode_questions.longest_substring_without_repeating_characters import (
    length_of_longest_substring,
)


def test_substring_in_front_should_return_3():
    string = "abcabcbb"
    expected = 3

    assert length_of_longest_substring(string) == expected


def test_same_chars_should_return_1():
    string = "bbbbbbbbb"
    expected = 1

    assert length_of_longest_substring(string) == expected


def test_single_char_should_return_1():
    string = "g"
    expected = 1

    assert length_of_longest_substring(string) == expected


def test_substring_in_middle_should_return_3():
    string = "pwwkew"
    expected = 3

    assert length_of_longest_substring(string) == expected


def test_substring_in_middle_should_return_4():
    string = "abccxyz"
    expected = 4

    assert length_of_longest_substring(string) == expected


def test_substring_in_middle_should_return_7():
    string = "abcdefg"
    expected = 7

    assert length_of_longest_substring(string) == expected
