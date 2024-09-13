"""
defining card effect functions
"""

from Main.Engine.Effects.effect_base import Effect  # This is the only import needed
from Main.Engine.Targeting.target_base import Target
from Main.Entity.game_state import GameState  # This is the only import needed


class Damage(Effect):
    """
    This class is used to determine the damage effect of a card.
    """

    def __init__(self, target: Target, amount: int) -> None:
        self.target = target()
        self.amount = amount

    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the damage effect of a card.
        """
        target = self.target.get_target(game_state)
        target.health -= self.amount


class DrawCard(Effect):
    """
    This class is used to determine the draw card effect of a card.
    """

    def __init__(self, target: Target, amount: int) -> None:
        self.target = target()
        self.amount = amount

    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the draw card effect of a card.
        """
        target = self.target.get_target(game_state)
        for _ in range(self.amount):
            if target.deck:
                card = target.deck.pop(0)
                if len(target.hand) < 10:
                    target.hand.append(card)
                else:
                    # Card is destroyed if hand size exceeds 10
                    print(f"Card {card} is destroyed because hand size exceeds 10.")
            else:
                # Apply fatigue damage if the deck is out of cards
                target.fatigue += 1
                target.health -= target.fatigue
                print(
                    f"{target} takes {target.fatigue} fatigue damage due to empty deck."
                )
