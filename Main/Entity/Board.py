from .Player import Player
from dataclasses import dataclass


@dataclass
class Board:
    player_1: Player
    player_2: Player
    active_player: int
