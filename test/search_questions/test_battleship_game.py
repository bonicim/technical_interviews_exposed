import pytest
from src.algorithms.search_questions.battleship_game import (
    setup_battlefield,
    fire_missile,
)


def test_setup_battlefield():
    ships_locations = [[(0, 0), (0, 0)], [(0, 9), (9, 9)], [(2, 1), (2, 3)]]

    expected_battlefield = [
        ["S1", None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, "S3", "S3", "S3", None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
    ]

    assert setup_battlefield(ships_locations) == expected_battlefield


def test_setup_battlefield_two_ships_adjacent():
    ships_locations = [[(2, 0), (2, 0)], [(2, 1), (2, 3)]]

    expected_battlefield = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        ["S1", "S2", "S2", "S2", None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]

    assert setup_battlefield(ships_locations) == expected_battlefield


def test_fire_missile_hit():
    battlefield = [
        ["S1", None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, "S3", "S3", "S3", None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
    ]

    x, y = 0, 9

    assert fire_missile(x, y, battlefield=battlefield) == "Hit"


def test_fire_missile_miss():
    battlefield = [
        ["S1", None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, "S3", "S3", "S3", None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
    ]

    x, y = 5, 7

    assert fire_missile(x, y, battlefield=battlefield) == "Miss"


def test_fire_missile_sink_one_cell_ship():
    battlefield = [
        ["S1", None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, "S3", "S3", "S3", None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
    ]

    x, y = 0, 0

    assert fire_missile(x, y, battlefield=battlefield) == "Sink"


def test_fire_missile_sink_large_vertical_ship():
    battlefield = [
        ["S1", None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, "S3", "S3", "S3", None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
        [None, None, None, None, None, None, None, None, None, "S2"],
    ]

    for row in range(9):
        assert fire_missile(row, 9, battlefield=battlefield) == "Hit"

    assert fire_missile(9, 9, battlefield=battlefield) == "Sink"


def test_setup_battlefield_sink_one_large_ship_adjacent():

    battlefield = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        ["S1", "S2", "S2", "S2", None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]

    # hit middle part of ship
    assert fire_missile(2, 2, battlefield=battlefield) == "Hit"
    # hit right
    assert fire_missile(2, 3, battlefield=battlefield) == "Hit"
    # hit final, left
    assert fire_missile(2, 1, battlefield=battlefield) == "Sink"
    # ensure that S1 was not hit
    assert battlefield[2][0] == "S1"
