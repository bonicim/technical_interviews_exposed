import pytest
from src.algorithms.pramp_questions.flatten_dict import flatten_dictionary


def test_simple():
    d = {"k1": 1, "k2": "foo"}
    expected = {"k1": "1", "k2": "foo"}

    actual = flatten_dictionary(d)

    assert actual == expected


def test_one_level_dict():
    d = {"k1": "foo", "k2": {"a": "bar"}}
    expected = {"k1": "foo", "k2.a": "bar"}

    actual = flatten_dictionary(d)

    assert actual == expected


def test_empty_one_level_dict():
    d = {"k1": "foo", "k2": {"": "bar"}}
    expected = {"k1": "foo", "k2": "bar"}

    actual = flatten_dictionary(d)

    assert actual == expected


# two-level dictinary
def test_two_level():

    d = {"k1": "foo", "k2": {"a": {"bar": "42", "goo": "df"}}}
    expected = {"k1": "foo", "k2.a.bar": "42", "k2.a.goo": "df"}

    actual = flatten_dictionary(d)

    assert actual == expected


def test_one_level():
    d = {"k1": "foo", "k2": {"a": "bar", "b": "roma"}}
    expected = {"k1": "foo", "k2.a": "bar", "k2.b": "roma"}

    actual = flatten_dictionary(d)

    assert actual == expected
