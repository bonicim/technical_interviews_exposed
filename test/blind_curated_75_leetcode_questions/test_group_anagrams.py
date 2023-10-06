import pytest

from src.algorithms.blind_curated_75_leetcode_questions.group_anagrams import (
    group_anagrams,
)


def test_regular_case():
    words = ["cat", "dog", "god"]

    actual = group_anagrams(words)

    assert actual == [{"cat"}, {"dog", "god"}]


def test_empty_list():
    words = []

    actual = group_anagrams(words)

    assert actual == []


def test_case_sensitive():
    words = ["Cat", "cat"]

    actual = group_anagrams(words)

    assert actual == [{"Cat"}, {"cat"}]


def test_duplicates():
    words = ["cat", "dog", "god", "god"]

    actual = group_anagrams(words)

    assert actual == [{"cat"}, {"dog", "god"}]
