import pytest

from src.algorithms.misc.daily_temperatures import get_days_to_warmer_temp


def test_example():
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]

    assert get_days_to_warmer_temp(temps) == expected


def test_temps_always_increasing():
    temps = [73, 74, 75]
    expected = [1, 1, 0]

    assert get_days_to_warmer_temp(temps) == expected


def test_temps_never_increase():
    temps = [70, 69, 68, 67, 30]
    expected = [0, 0, 0, 0, 0]

    assert get_days_to_warmer_temp(temps) == expected


def test_temps_single():
    temps = [70]
    expected = [0]

    assert get_days_to_warmer_temp(temps) == expected


def test_temps_increase_at_end():
    temps = [70, 50, 45, 33, 30, 100]
    expected = [5, 4, 3, 2, 1, 0]

    assert get_days_to_warmer_temp(temps) == expected


def test_temps_seattle_fall_weather_ten_days():
    temps = [45, 45, 41, 41, 43, 41, 45, 45, 49, 49]
    expected = [8, 7, 2, 1, 2, 1, 2, 1, 0, 0]

    assert get_days_to_warmer_temp(temps) == expected
