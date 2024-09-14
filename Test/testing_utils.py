from Main.Entity.player_base import Player
from Main.Entity.game_state import GameState


def create_game():
    """
    This function is used to create a game state for testing.
    """
    p_1 = Player([], [1, 1, 1], [])
    p_2 = Player([], [1, 1, 1], [])
    game = GameState(p_1, p_2, p_1)
    return game
