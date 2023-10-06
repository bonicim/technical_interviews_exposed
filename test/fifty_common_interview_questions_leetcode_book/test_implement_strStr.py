import pytest
from src.algorithms.fifty_common_interview_questions_leetcode_book.str_str import (
    str_str,
)


def test_should_return_2():
    haystack = "hello"
    needle = "ll"

    assert str_str(haystack, needle) == 2


def test_should_return_negative_1():
    haystack = "aaaaaaaaaaaaaa"
    needle = "bba"

    assert str_str(haystack, needle) == -1


def test_matching_string_at_end_should_return_3():
    haystack = "helllo"
    needle = "llo"

    assert str_str(haystack, needle) == 3


def test_needle_at_end_of_haystack_return_4():
    haystack = "hello"
    needle = "o"

    assert str_str(haystack, needle) == 4


def test_empty_needle_should_return_0():
    assert str_str("fghgffdsgfsdgdf", "") == 0


def test_empty_haystack_should_return_negative_1():
    assert str_str("", "fdafdsfasdf") == -1


def test_empty_needle_empty_haystack_should_return_0():
    assert str_str("", "") == 0


def test_needle_greater_than_haystack_should_return_negative_1():
    assert str_str("dfddf", "fdsafadsfasdfadsfadsf") == -1


def test_multiple_needles_in_haystack():
    haystack = "mississippi"
    needle = "issi"

    assert str_str(haystack, needle) == 1


def test_long_strings_should_return_negative_1():
    haystack = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    needle = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX"

    assert str_str(haystack, needle) == -1
