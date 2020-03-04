import pytest

from src.algorithms.interview_cake_questions.reverse_words import reverse_words


def test_example():
    message = [
        "c",
        "a",
        "k",
        "e",
        " ",
        "p",
        "o",
        "u",
        "n",
        "d",
        " ",
        "s",
        "t",
        "e",
        "a",
        "l",
    ]

    expected = "steal pound cake"

    assert reverse_words(message) == expected


def test_example2():
    message = [
        "t",
        "h",
        "e",
        " ",
        "e",
        "a",
        "g",
        "l",
        "e",
        " ",
        "h",
        "a",
        "s",
        " ",
        "l",
        "a",
        "n",
        "d",
        "e",
        "d",
    ]

    expected = "landed has eagle the"

    assert reverse_words(message) == expected


def test_simple_test():
    message = [" ", " "]
    expected = "".join([" ", " "])

    assert reverse_words(message) == expected


def test_two_spaces():
    message = ["a", " ", " ", "b"]
    expected = "".join(["b", " ", " ", "a"])

    assert reverse_words(message) == expected


def test_two_spaces_spaced_out():
    message = ["a", " ", " ", "b", " ", " ", "f"]
    expected = "".join(["f", " ", " ", "b", " ", " ", "a"])

    assert reverse_words(message) == expected


def test_two_spaces_with_long_words():
    message = ["abv", " ", " ", "qwe", " ", " ", "ffff"]
    expected = "".join(["ffff", " ", " ", "qwe", " ", " ", "abv"])

    assert reverse_words(message) == expected


def test_one_word():
    message = ["h", "e", "l", "l", "o"]
    expected = "".join(["h", "e", "l", "l", "o"])
    assert reverse_words(message) == expected


def test_three_words():
    message = [
        "p",
        "e",
        "r",
        "f",
        "e",
        "c",
        "t",
        " ",
        "m",
        "a",
        "k",
        "e",
        "s",
        " ",
        "p",
        "r",
        "a",
        "c",
        "t",
        "i",
        "c",
        "e",
    ]
    expected = "".join(
        [
            "p",
            "r",
            "a",
            "c",
            "t",
            "i",
            "c",
            "e",
            " ",
            "m",
            "a",
            "k",
            "e",
            "s",
            " ",
            "p",
            "e",
            "r",
            "f",
            "e",
            "c",
            "t",
        ]
    )
    assert reverse_words(message) == expected


def test_long_phrase():
    message = [
        "y",
        "o",
        "u",
        " ",
        "w",
        "i",
        "t",
        "h",
        " ",
        "b",
        "e",
        " ",
        "f",
        "o",
        "r",
        "c",
        "e",
        " ",
        "t",
        "h",
        "e",
        " ",
        "m",
        "a",
        "y",
    ]
    expected = "".join(
        [
            "m",
            "a",
            "y",
            " ",
            "t",
            "h",
            "e",
            " ",
            "f",
            "o",
            "r",
            "c",
            "e",
            " ",
            "b",
            "e",
            " ",
            "w",
            "i",
            "t",
            "h",
            " ",
            "y",
            "o",
            "u",
        ]
    )

    assert reverse_words(message) == expected


def test_really_long_phrase():
    message = [
        "g",
        "r",
        "e",
        "a",
        "t",
        "e",
        "s",
        "t",
        " ",
        "n",
        "a",
        "m",
        "e",
        " ",
        "f",
        "i",
        "r",
        "s",
        "t",
        " ",
        "e",
        "v",
        "e",
        "r",
        " ",
        "n",
        "a",
        "m",
        "e",
        " ",
        "l",
        "a",
        "s",
        "t",
    ]
    expected = "".join(
        [
            "l",
            "a",
            "s",
            "t",
            " ",
            "n",
            "a",
            "m",
            "e",
            " ",
            "e",
            "v",
            "e",
            "r",
            " ",
            "f",
            "i",
            "r",
            "s",
            "t",
            " ",
            "n",
            "a",
            "m",
            "e",
            " ",
            "g",
            "r",
            "e",
            "a",
            "t",
            "e",
            "s",
            "t",
        ]
    )

    assert reverse_words(message) == expected
