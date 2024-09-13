from Main.Engine.Targeting.target_func import FreindlyHero
from Main.Engine.Effects.effect_func import Damage
from Main.Entity.player_base import Player
from Main.Entity.game_state import GameState


def create_game():
    """
    This function is used to create a game state for testing.
    """
    p_1 = Player([], [], [], [])
    p_2 = Player([], [], [], [])
    game = GameState(p_1, p_2, p_1)
    return game


def test_damage():
    """
    This function is used to test the damage effect of a card.
    """
    game = create_game()
    damage = Damage(FreindlyHero, 5)
    damage.execute(game)
    assert game.player_1.health == 25  # The player should have 25 health left
