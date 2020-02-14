import pytest
from src.algorithms.pramp_questions.award_budget_cuts import find_grants_cap


def test_regular_example():
    grants = [2.0, 4.0]
    new_budget = 3.0
    expected = 1.5

    actual = find_grants_cap(grants, new_budget)

    assert actual == expected


def test_bigger_list():
    grants = [2.0, 100.0, 50.0, 120.0, 1000.0]
    new_budget = 190.0
    expected = 47.0

    actual = find_grants_cap(grants, new_budget)

    assert actual == expected


def test_original_budget_within_new_budget():
    grants = [5.5, 6.4, 7.5, 8.5, 9.1, 4.5]
    new_budget = float(45.22222)
    expected = 9.1

    actual = find_grants_cap(grants, new_budget)

    assert actual == expected
