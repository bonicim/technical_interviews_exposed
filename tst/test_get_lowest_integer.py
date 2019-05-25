import pytest
from src.algorithms.get_lowest_integer import get_lowest_integer

def test_typical_case_lowest_integer():
    assert get_lowest_integer("746209249", 5) == "0249"
    assert get_lowest_integer("43597658", 2) == "357658"

def test_zero_remove_lowest_intger():
    assert get_lowest_integer("839275", 0) == "839275"

def test_greater_than_size_lowest_integer():
    assert get_lowest_integer("24", 3) == "0"

def test_negative_remove_lowest_integer():
    assert get_lowest_integer("3334", -3) == "3334"

def test_remove_size_equal_lowest_integer():
    assert get_lowest_integer("4321", 4) == "0"