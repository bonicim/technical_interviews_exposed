from src.algorithms.interview_cake_questions.apple_stocks import calculate_max_profit


def test_example():
    prices = [10, 7, 5, 8, 11, 9]
    expected = 6

    assert calculate_max_profit(prices) == expected


def test_all_decreasing_prices():
    prices = [7, 6, 4, 3, 1]
    expected = 0

    assert calculate_max_profit(prices) == expected


def test_no_change():
    prices = [7, 7, 7, 7, 7, 7, 7, 7]
    expected = 0

    assert calculate_max_profit(prices) == expected
