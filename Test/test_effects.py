"""
test effects
"""

from Test.testing_utils import create_game
from Main.Engine.Targeting.target_func import EnemyHero, FreindlyHero
from Main.Engine.Effects.effect_func import DrawCard, Damage


def test_draw():
    """
    This function is used to test the draw card effect of a card.
    """
    game = create_game()
    draw = DrawCard(FreindlyHero, 1)
    draw.execute(game)
    assert len(game.player_1.hand) == 1  # The player should have 1 card in hand


def test_fatigue_damage():
    """
    This function is used to test the fatigue damage effect when a player tries to draw from an empty deck.
    """
    game = create_game()
    game.player_1.deck = []  # Empty the player's deck
    draw = DrawCard(FreindlyHero, 1)
    draw.execute(game)
    assert (
        game.player_1.health < game.player_1.max_health
    )  # The player should take fatigue damage


def test_multiple_draws():
    """
    This function is used to test drawing multiple cards.
    """
    game = create_game()
    draw = DrawCard(FreindlyHero, 3)
    draw.execute(game)
    assert len(game.player_1.hand) == 3  # The player should have 3 cards in hand


def test_draw_with_partial_deck():
    """
    This function is used to test drawing cards when the deck has fewer cards than the draw amount.
    """
    game = create_game()
    game.player_1.deck = [1]  # Only 1 card in the deck
    draw = DrawCard(FreindlyHero, 2)
    draw.execute(game)
    assert len(game.player_1.hand) == 1  # The player should have 1 card in hand
    assert (
        game.player_1.health < game.player_1.max_health
    )  # The player should take fatigue damage for the second card


def test_damage():
    """
    This function is used to test the damage effect of a card.
    """
    game = create_game()
    damage = Damage(FreindlyHero, 5)
    damage.execute(game)
    assert game.player_1.health == 25  # The player should have 25 health left


def test_draw_chain():
    """
    function to test chaining draw/effects.
    """

    game = create_game()
    draw = DrawCard(FreindlyHero, 3) + DrawCard(EnemyHero, 4)
    draw.execute
