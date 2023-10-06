import pytest
from src.algorithms.vulcan_questions.missing_integer_v2 import missing_integer_v2


def test_example1():
    arr = [1, 1, 2, 3, 3]
    k = 3

    assert missing_integer_v2(arr, k) is True


def test_example2():
    arr = [1, 1, 3]
    k = 2

    assert missing_integer_v2(arr, k) is False


def test_example3():
    arr = [4, 5, 6]
    k = 6

    assert missing_integer_v2(arr, k) is False


def test_example4():
    arr = [0, 1, 2, 3]
    k = 3

    assert missing_integer_v2(arr, k) is True


def test_example5():
    arr = [0, 1, 2, 3]
    k = 4

    assert missing_integer_v2(arr, k) is False


def test_example6():
    arr = [0, 1, 1, 2, 3]
    k = 3

    assert missing_integer_v2(arr, k) is True


def test_example7():
    arr = [0, 1, 1, 2, 3]
    k = 2

    assert missing_integer_v2(arr, k) is True


def test_example8():
    arr = [0, 1, 2, 3]
    k = 2

    assert missing_integer_v2(arr, k) is True


def test_example9():
    arr = [1]
    k = 1

    assert missing_integer_v2(arr, k) is True


def test_example10():
    arr = [0]
    k = 1

    assert missing_integer_v2(arr, k) is False


def test_example11():
    arr = [2, 3, 4, 5, 6, 7]
    k = 1

    assert missing_integer_v2(arr, k) is False


def test_example12():
    arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
    k = 7

    assert missing_integer_v2(arr, k) is False


def test_example13():
    arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
    k = 4

    assert missing_integer_v2(arr, k) is False
