import pytest
from src.algorithms.is_palindrome import is_palindrome


def test_true():
    assert is_palindrome("aba") is True
