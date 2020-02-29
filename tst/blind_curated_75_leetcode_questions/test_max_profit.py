import pytest

from src.algorithms.blind_curated_75_leetcode_questions.max_profit import max_profit


def test_example():
    prices = [10, 7, 5, 8, 11, 9]
    expected = 6

    assert max_profit(prices) == expected


def test_all_decreasing_prices():
    prices = [7, 6, 4, 3, 1]
    expected = 0

    assert max_profit(prices) == expected


def test_no_change():
    prices = [7, 7, 7, 7, 7, 7, 7, 7]
    expected = 0

    assert max_profit(prices) == expected


def test_one_price():
    prices = [7]
    expected = 0

    assert max_profit(prices) == expected
