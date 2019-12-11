import pytest

from src.algorithms.interview_cake_questions.sort_scores import sort_scores


def test_example():
    scores = [37, 89, 41, 65, 91, 53]
    perfect_score = 100
    expected = [91, 89, 65, 53, 41, 37]

    assert sort_scores(scores, perfect_score) == expected


def test_duplicate_scores():
    scores = [35, 75, 75, 63]
    perfect_score = 100
    expected = [75, 75, 63, 35]

    assert sort_scores(scores, perfect_score) == expected
