import pytest
from src.algorithms.string_questions.compress_string import compress_string


def test_example():
    string = "aabcccccaaa"
    expected = "a2b1c5a3"

    assert compress_string(string) == expected


def test_string_already_compressed():
    string = "a"
    expected = "a"

    assert compress_string(string) == expected


def test_string_all_singles_no_duplicates():
    string = "dkhgew"
    expected = "dkhgew"

    assert compress_string(string) == expected


def test_string_duplicates_already_compressed():
    string = "bccc"
    expected = "bccc"

    assert compress_string(string) == expected


def test_string_duplicates_needs_compression():
    string = "bcccc"
    expected = "b1c4"

    assert compress_string(string) == expected
