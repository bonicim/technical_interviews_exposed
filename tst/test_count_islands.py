import pytest
from src.algorithms.count_islands import count_islands


def test_big_island():
    mmap = [
        ["O", "O", "O", "O", "O"],
        ["O", "L", "L", "O", "O"],
        ["O", "L", "L", "O", "O"],
    ]
    assert count_islands(mmap) == 1


def test_small_island():
    mmap = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "L", "O"],
        ["O", "O", "O", "O", "O"],
    ]
    assert count_islands(mmap) == 1


def test_two_islands():
    mmap = [
        ["O", "O", "L", "O", "O"],
        ["O", "L", "L", "O", "O"],
        ["O", "O", "O", "O", "L"],
    ]
    assert count_islands(mmap) == 2


def test_no_islands():
    mmap = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
    ]
    assert count_islands(mmap) == 0


def test_empty_map():
    mmap = []
    assert count_islands(mmap) == 0


def test_entire_map_is_island():
    mmap = [["L", "L"], ["L", "L"]]
    assert count_islands(mmap) == 1


def test_diagonal_island():
    mmap = [["L", "O"], ["O", "L"]]
    assert count_islands(mmap) == 2
