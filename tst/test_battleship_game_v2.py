import pytest
from src.algorithms.battleship_game import BattleshipGame


def test_miss():
    ships = [
        {"submarine": {(0, 0), (0, 1), (0, 2)}},
        {"carrier": {(10, 0), (10, 1), (10, 2), (10, 3)}},
    ]

    battleship_game = BattleshipGame(ships)

    assert battleship_game.fire_missile((0, 3)) == "miss"


def test_hit():
    ships = [
        {"submarine": {(0, 0), (0, 1), (0, 2)}},
        {"carrier": {(10, 0), (10, 1), (10, 2), (10, 3)}},
    ]

    battleship_game = BattleshipGame(ships)

    assert battleship_game.fire_missile((0, 0)) == "hit"


def test_sunk():
    ships = [
        {"submarine": {(0, 0), (0, 1), (0, 2)}},
        {"carrier": {(10, 0), (10, 1), (10, 2), (10, 3)}},
    ]

    battleship_game = BattleshipGame(ships)

    assert battleship_game.fire_missile((0, 0)) == "hit"
    assert battleship_game.fire_missile((0, 1)) == "hit"
    assert battleship_game.fire_missile((0, 2)) == "sunk"


def test_win():
    ships = [
        {"submarine": {(0, 0), (0, 1), (0, 2)}},
        {"carrier": {(10, 0), (10, 1), (10, 2), (10, 3)}},
    ]

    battleship_game = BattleshipGame(ships)

    assert battleship_game.fire_missile((0, 0)) == "hit"
    assert battleship_game.fire_missile((0, 1)) == "hit"
    assert battleship_game.fire_missile((0, 2)) == "sunk"

    assert battleship_game.fire_missile((10, 0)) == "hit"
    assert battleship_game.fire_missile((10, 1)) == "hit"
    assert battleship_game.fire_missile((10, 2)) == "hit"
    assert battleship_game.fire_missile((10, 3)) == "win"
