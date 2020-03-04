import pytest
import sys

from src.algorithms.recursion_questions.minimum_steps_to_one import minimum_steps_to_one


def test_4_should_return_2():
    n = 4
    expected = 2

    actual = minimum_steps_to_one(n)

    assert actual == expected


def test_1_should_return_0():
    n = 1
    expected = 0

    actual = minimum_steps_to_one(n)

    assert actual == expected


def test_7_should_return_3():
    n = 7
    expected = 3

    actual = minimum_steps_to_one(n)

    assert actual == expected


def test_10_should_return_3():
    n = 10
    expected = 3

    actual = minimum_steps_to_one(n)

    assert actual == expected


def test_1000_call_stack_limit():
    n = 1000
    expected = 9

    actual = minimum_steps_to_one(n)

    assert actual == expected


def test_really_big_number():
    n = 1000000
    expected = 19

    actual = minimum_steps_to_one(n)

    assert actual == expected
