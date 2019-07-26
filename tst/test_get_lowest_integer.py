import pytest
from src.algorithms.get_lowest_integer import get_lowest_integer

def test_typical_case_lowest_integer():
    assert get_lowest_integer("746209249", 5) == "0249"

def test_multiples_random_number():
    assert get_lowest_integer("43597658", 1) == "3597658"
    assert get_lowest_integer("43597658", 2) == "357658"
    assert get_lowest_integer("43597658", 3) == "35658"
    assert get_lowest_integer("43597658", 4) == "3558"
    assert get_lowest_integer("43597658", 5) == "355"
    assert get_lowest_integer("43597658", 6) == "35"
    assert get_lowest_integer("43597658", 7) == "3"
    assert get_lowest_integer("43597658", 8) == "0"


def test_multiple_cases_big_number_in_front():
    assert get_lowest_integer("678123", -1) == "678123"
    assert get_lowest_integer("678123", 0) == "678123"
    assert get_lowest_integer("678123", 1) == "67123"
    assert get_lowest_integer("678123", 1) == "67123"
    assert get_lowest_integer("678123", 2) == "6123"
    assert get_lowest_integer("678123", 3) == "123"
    assert get_lowest_integer("678123", 4) == "12"
    assert get_lowest_integer("678123", 5) == "1"
    assert get_lowest_integer("678123", 6) == "0"
    assert get_lowest_integer("678123", 42) == "0"

def test_multiple_cases_small_numbers_in_front():
    assert get_lowest_integer("123678", 1) == "12367"
    assert get_lowest_integer("123678", 2) == "1236"
    assert get_lowest_integer("123678", 3) == "123"
    assert get_lowest_integer("123678", 4) == "12"
    assert get_lowest_integer("123678", 5) == "1"
    assert get_lowest_integer("123678", 6) == "0"

def test_big_numbers_in_front():
    assert get_lowest_integer("678123", 3) == "123"

def test_zero_remove_lowest_intger():
    assert get_lowest_integer("839275", 0) == "839275"

def test_greater_than_size_lowest_integer():
    assert get_lowest_integer("24", 3) == "0"

def test_really_greater_than_size_lowest_integer():
    assert get_lowest_integer("4321", 6759867835) == "0"

def test_negative_remove_lowest_integer():
    assert get_lowest_integer("3334", -3) == "3334"

def test_remove_size_equal_lowest_integer():
    assert get_lowest_integer("4321", 4) == "0"