import pytest

from src.algorithms.interview_cake_questions.is_fifo import is_fifo


def test_example():
    takeout = [1, 3, 5]
    dine_in = [2, 4, 6]
    served = [1, 2, 4, 6, 5, 3]

    assert is_fifo(takeout, dine_in, served) is False


def test_example_should_be_true():
    takeout = [1, 3, 5]
    dine_in = [2, 4, 6]
    served = [1, 2, 3, 5, 4, 6]

    assert is_fifo(takeout, dine_in, served) is True


def test_order_taken_but_not_served():
    takeout = [1, 3, 5]
    dine_in = [2, 4, 6]
    served = [1, 2, 3, 4, 6]

    assert is_fifo(takeout, dine_in, served) is False
