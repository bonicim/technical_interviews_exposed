import pytest

from src.algorithms.get_list_anagrams import get_list_anagrams


def test_regular_case():
    words = ["cat", "dog", "god"]

    actual = get_list_anagrams(words)

    assert actual == [{"cat"}, {"dog", "god"}]


def test_empty_list():
    words = []

    actual = get_list_anagrams(words)

    assert actual == []


def test_case_sensitive():
    words = ["Cat", "cat"]

    actual = get_list_anagrams(words)

    assert actual == [{"Cat"}, {"cat"}]


def test_duplicates():
    words = ["cat", "dog", "god", "god"]

    actual = get_list_anagrams(words)

    assert actual == [{"cat"}, {"dog", "god"}]
