import pytest
from src.algorithms.tape_equilibrium import get_min_from_tape

def test_regular_case():
    arr = [3, 1, 2, 4, 3]
    assert get_min_from_tape(arr) == 1