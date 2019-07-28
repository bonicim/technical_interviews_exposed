import pytest
import random

from src.algorithms.find_missing_integer import find_missing_integer

def test_example_1():
    arr = [1, 3, 6, 4, 1, 2]
    actual = find_missing_integer(arr)
    
    assert actual == 5

def test_example_2():
    arr = [-1, -3]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_example_3():
    arr = [1, 3, 2]
    actual = find_missing_integer(arr)
    
    assert actual == 4

def test_simple():
    arr = [2, 3, 4, 5]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_all_neg():
    arr = [-1, -3, -2]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_simple_single():
    arr = [2]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_simple_single_v2():
    arr = [1]
    actual = find_missing_integer(arr)
    
    assert actual == 2

def test_simple_single_zero():
    arr = [0]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_simple_single_neg():
    arr = [-1]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_extreme_positive_single():
    arr = [1000000]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_extreme_negative_single():
    arr = [-1000000]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_extreme_min_max():
    arr = [1000000, -1000000]
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_shuffled_positive_only():
    arr1 = [x for x in range(11)]
    arr2 = [x for x in range(12, 21)]
    arr = arr1 + arr2
    random.shuffle(arr)
    actual = find_missing_integer(arr)
    
    assert actual == 11

def test_shuffled_negative_only():
    arr = [x for x in range(-1, -11, -1)]
    random.shuffle(arr)
    actual = find_missing_integer(arr)
    
    assert actual == 1

def test_shuffled_pos_neg_zero():
    arr1 = [x for x in range(-1, -11, -1)]
    arr2 = [x for x in range(1, 101)]
    arr = arr1 + arr2
    random.shuffle(arr)
    actual = find_missing_integer(arr)
    
    assert actual == 101
def test_empty_list():
    arr = []
    actual = find_missing_integer(arr)

    assert actual == 1