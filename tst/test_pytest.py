import pytest
from src.algorithms import (
    count_islands, get_lowest_integer)

def test_big_island():
    mmap = [
        ['O','O','O','O','O'],
        ['O','L','L','L','O'],
        ['O','L','L','O','O']
    ]    
    assert count_islands(mmap) == 5

def test_small_island():
    mmap = [
        ['O','O','O','O','O'],
        ['O','O','O','L','O'],
        ['O','O','O','O','O']
    ]    
    assert count_islands(mmap) == 1

def test_two_islands():
    mmap = [
        ['O','O','L','O','O'],
        ['O','L','L','L','O'],
        ['O','O','O','O','L']
    ]    
    assert count_islands(mmap) == 4

def test_no_islands():
    mmap = [
        ['O','O','O','O','O'],
        ['O','O','O','O','O'],
        ['O','O','O','O','O']
    ]    
    assert count_islands(mmap) == 0

def test_empty_map():
    mmap = []    
    assert count_islands(mmap) == 0

def test_unequal_lengths_rows():
    mmap = [
        ['O','O','O','O','O','O','O','O'],
        ['O','L','L','L','O'],
        ['O','L','L','O','O']
    ]    
    assert count_islands(mmap) == 5

    mmap = [
        ['O','L','L','L','O'],
        ['O','O','O','O','O','O','O','O'],
        ['O','L','L','O','O']
    ]    
    assert count_islands(mmap) == 3

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

