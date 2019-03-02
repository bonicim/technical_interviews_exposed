from src.count_islands import count_islands

def test_big_island():
    mmap = [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,1,0,0]
    ]    
    assert count_islands(mmap) == 5

def test_small_island():
    mmap = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,1]
    ]    
    assert count_islands(mmap) == 1

def test_two_islands():
    mmap = [
        [0,0,1,1,0],
        [0,1,1,0,0],
        [0,0,0,0,1]
    ]    
    assert count_islands(mmap) == 4

def test_no_islands():
    mmap = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]    
    assert count_islands(mmap) == 0

def test_empty_map():
    mmap = []    
    assert count_islands(mmap) == 0

def test_unequal_lengths_rows():
    mmap = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,0,0]
    ]    
    assert count_islands(mmap) == 2

    mmap = [
        [0,0,0,1,1],
        [0,0,0,0,1,1,1,1],
        [0,1,1,0,0]
    ]    
    assert count_islands(mmap) == 6