from src.count_islands import count_islands

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