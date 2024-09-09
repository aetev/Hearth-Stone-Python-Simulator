from .Player import Player
from dataclasses import dataclass


@dataclass
class GameState:
    player_1: Player
    player_2: Player
    active_player: None
