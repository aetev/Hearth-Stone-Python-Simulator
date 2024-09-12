from Main.Engine.target_func import Target
from Main.Entity.game_state import GameState


class effect:
    def __init__(self, target: Target, amount: int):
        self.target = target
        self.amount = amount

    def exectute(self, game_state: GameState):
        pass


class damage(effect):
    def execute(self, game_state: GameState):
        target = self.target.get_target(game_state)
        target.health -= self.amount
        pass
