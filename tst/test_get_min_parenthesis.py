import pytest

from src.algorithms.get_min_parenthesis import get_min_parenthesis


def test_simple_case_should_return_1():
    string = "()("

    assert get_min_parenthesis(string) == 1


def test_simple_case_should_return_2():
    string = "((()"

    assert get_min_parenthesis(string) == 2


def test_complete_parenthesis_should_return_0():
    string = "()"

    assert get_min_parenthesis(string) == 0


def test_multiple_complete_parenthesis_should_return_0():
    string = "()(((())))"

    assert get_min_parenthesis(string) == 0


def test_single_open_parenthesis_should_return_1():
    string = "("

    assert get_min_parenthesis(string) == 1


def test_single_closed_parenthesis_should_return_1():
    string = ")"

    assert get_min_parenthesis(string) == 1


def test_backwards_complete_parenthesis_should_return_2():
    string = ")("

    assert get_min_parenthesis(string) == 2


def test_empty_string_should_return_0():
    assert get_min_parenthesis("") == 0


def test_complex_parenthesis_should_return_4():
    string = "()))(("

    assert get_min_parenthesis(string) == 4
