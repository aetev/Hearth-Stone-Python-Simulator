"""
This file is used to test the entities.
"""

from Main.Entity.game_state import GameState  # This is the only import needed
from Main.Entity.player_base import Player  # import the Player class


def test_game():
    """
    This function is used to test the game and player classes
    """
    p_1 = Player([], [], [])
    p_2 = Player([], [], [])
    game_state = GameState(p_1, p_2, p_1)
    assert game_state.player_1 == p_1
    assert game_state.player_2 == p_2
    assert game_state.active_player == p_1
    print("TestGameAndPlayer passed")
