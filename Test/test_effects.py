from Main.Engine.Targeting.target_func import FreindlyHero
from Main.Engine.Effects.effect_func import DrawCard
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


def test_draw():
    """
    This function is used to test the draw card effect of a card.
    """
    game = create_game()
    draw = DrawCard(FreindlyHero, 1)
    draw.execute(game)
    assert len(game.player_1.hand) == 1  # The player should have 1 card in hand
