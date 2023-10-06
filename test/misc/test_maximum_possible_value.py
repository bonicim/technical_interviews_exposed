import pytest
from src.algorithms.misc.maximum_possible_value import maximum_possible_value


def test_example():
    num = 268
    expected = 5268

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example2():
    num = 670
    expected = 6750

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example2():
    num = 670
    expected = 6750

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example3():
    num = 0
    expected = 50

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example4():
    num = -999
    expected = -5999

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example5():
    num = 5
    expected = 55

    actual = maximum_possible_value(num)

    assert actual == expected


def test_example6():
    num = -5
    expected = -55

    actual = maximum_possible_value(num)

    assert actual == expected
