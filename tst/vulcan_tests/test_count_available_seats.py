import pytest

from src.algorithms.vulcan_questions.plane_seat_reservation import (
    plane_seat_reservations,
)


def test_empty_case():
    actual = plane_seat_reservations("", 1)
    assert actual == 3


def test_left_most_reserved_case():
    actual = plane_seat_reservations("5A", 10)
    assert actual == 29


def test_middle_left_most_reserved_case():
    actual = plane_seat_reservations("3D", 3)
    assert actual == 9


def test_middle_left_and_right_most_reserved_case():
    actual = plane_seat_reservations("1D 1G", 4)
    assert actual == 11


def test_middle_left_mid_reserved_case():
    actual = plane_seat_reservations("1E", 7)
    assert actual == 20


def test_all_middle_reserved_case():
    actual = plane_seat_reservations("1D 1E 1F 1G", 3)
    assert actual == 8
