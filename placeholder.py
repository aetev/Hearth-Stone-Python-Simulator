class Target:
  def get_target(game_state: GameState):
    pass

class freindly_hero(Target):
  def get_target(game_state: GameState):
    return game_state.player_1

class effect:
  def __init__(self, target: Target, amount: int):
    self.target = target
    self.amount = amount

  def exectute(self, game_state: GameState):
    pass

class damage(effect):
  def execute(self, game_state: GameState
    target = self.target.get_target(game_state)
    target.health -= self.amount
    pass
