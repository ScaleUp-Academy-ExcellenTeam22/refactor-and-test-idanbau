import pytest

import main


@pytest.fixture(scope="module")
def get_game():
    return main.Snake


def test_game_over(get_game):
    assert get_game.is_game_ended([0, 0], [[0, 0], [1, 1]])


def test_is_out_of_boarders(get_game):
    assert get_game.is_out_of_boarders([400, -1])
