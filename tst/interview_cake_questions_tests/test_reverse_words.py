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
