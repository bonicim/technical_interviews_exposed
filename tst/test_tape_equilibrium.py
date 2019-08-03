import pytest
from src.algorithms.tape_equilibrium import get_min_from_tape

def test_regular():
    arr = [3, 1, 2, 4, 3]
    assert get_min_from_tape(arr) == 1

def test_sorted_positive():
    arr = [1, 2, 3]
    assert get_min_from_tape(arr) == 0

def test_one_negative_case():
    arr = [-100, 50, 60, 10]
    assert get_min_from_tape(arr) == 0