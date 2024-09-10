from Main.Entity.GameState import GameState


class Target:
    def get_target(game_state: GameState):
        pass


class freindly_hero(Target):
    def get_target(game_state: GameState):
        return game_state.player_1
