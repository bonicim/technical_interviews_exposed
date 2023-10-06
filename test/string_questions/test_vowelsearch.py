import pytest
from src.algorithms.string_questions.vowel_search import contains_vowel


def test_vowel():
    assert 2 + 2 == 4


def test_emptylist_shouldreturn_false():
    arr = []
    assert contains_vowel(arr) is False


def test_one_string_no_vowel_inarr_shouldreturn_false():
    arr = ["fff"]
    assert contains_vowel(arr) is False


def test_one_string_vowel_inarr_shouldreturn_true():
    arr = ["cat"]
    assert contains_vowel(arr) is True


def test_all_consonants_inarr_shouldreturn_false():
    arr = ["fff", "ttt", "cry"]
    assert contains_vowel(arr) is False


def test_all_vowels_inarr_shouldreturn_True():
    arr = ["cat", "dog", "apple"]
    assert contains_vowel(arr) is True
