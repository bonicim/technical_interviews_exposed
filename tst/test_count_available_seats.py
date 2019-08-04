import pytest
from src.algorithms.count_available_seats import count_available_seats

def test_empty_case():
    actual = count_available_seats("", 1)
    assert actual == 3

def test_left_most_reserved_case():
    actual = count_available_seats("5A", 10)
    assert actual == 29

def test_middle_left_most_reserved_case():
    actual = count_available_seats("3D", 3)
    assert actual == 9

def test_middle_left_and_right_most_reserved_case():
    actual = count_available_seats("1D 1G", 4)
    assert actual == 11

def test_middle_left_mid_reserved_case():
    actual = count_available_seats("1E", 7)
    assert actual == 20

def test_all_middle_reserved_case():
    actual = count_available_seats("1D 1E 1F 1G", 3)
    assert actual == 8


