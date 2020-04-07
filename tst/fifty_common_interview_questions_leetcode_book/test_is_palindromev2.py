from src.algorithms.fifty_common_interview_questions_leetcode_book.is_palindrome import (
    is_palindrome,
)


def test_should_be_true():
    string = "A man, a plan, a canal: Panama"
    assert is_palindrome(string) is True

    string = "AmanaplanacanalPanama"
    assert is_palindrome(string) is True

    assert is_palindrome("111121111") is True


def test_should_be_false():
    string = "race a car"
    assert is_palindrome(string) is False

    assert is_palindrome("112") is False


def test_only_non_alpha_numeric_should_be_true():
    assert is_palindrome(":") is True
    assert is_palindrome(" ") is True


def test_empty_string_should_be_true():
    assert is_palindrome("") is True


def test_non_alpha_numeric_should_be_true():
    assert is_palindrome(",;") is True
    assert is_palindrome("%") is True
    assert is_palindrome(",,,,,,,,,") is True
    assert is_palindrome(",;^$#") is True
