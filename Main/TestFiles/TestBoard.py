from Main.Entity.GameState import GameState


def test_game_state(self):
    game_state = GameState()
    assert game_state.player_1 is None
