import pytest
from src.algorithms.tape_equilibrium import is_palindrome


def test_true():
    assert is_palindrome("aba") is True