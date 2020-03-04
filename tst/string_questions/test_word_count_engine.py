import pytest

from src.algorithms.string_questions.word_count_engine import word_count_engine


def test_example():
    message = (
        "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    )
    expected = [
        ["practice", "3"],
        ["perfect", "2"],
        ["makes", "1"],
        ["youll", "1"],
        ["only", "1"],
        ["get", "1"],
        ["by", "1"],
        ["just", "1"],
    ]

    actual = word_count_engine(message)

    assert actual == expected
