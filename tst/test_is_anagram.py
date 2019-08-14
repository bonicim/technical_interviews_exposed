import pytest

from src.algorithms.is_anagram import is_anagram

def test_example():
    w1 = "table"
    w2= "bleat"
    actual = is_anagram(w1, w2)

    assert actual is True

def test_no_anagram_same_length():
    w1 = "tabla"
    w2= "bleat"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_no_anagram_diff_length():
    w1 = "tfgfkjgfdjgljsfdlgkd"
    w2= "bleat"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_one_empty_string():
    w1 = ""
    w2= "bleat"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_two_empty_string():
    w1 = ""
    w2= ""
    actual = is_anagram(w1, w2)

    assert actual is True

def test_duplicate_string():
    w1 = "bleat"
    w2= "bleat"
    actual = is_anagram(w1, w2)

    assert actual is True

def test_repetition():
    w1 = "are"
    w2= "area"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_different_cases_1():
    w1 = "China"
    w2= "china"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_different_cases_2():
    w1 = "China"
    w2= "China"
    actual = is_anagram(w1, w2)

    assert actual is True

def test_different_cases_3():
    w1 = "CHINACHINACHINA"
    w2= "China"
    actual = is_anagram(w1, w2)

    assert actual is False

def test_different_all_caps_1():
    w1 = "TAIWANNUMBERONE"
    w2 = "TAIWANNUMBERONE"
    actual = is_anagram(w1, w2)

    assert actual is True

def test_different_all_caps_2():
    w1 = "TAIWANNUMBERONE"
    w2 = "TAIWANNUMBERone"
    actual = is_anagram(w1, w2)

    assert actual is False