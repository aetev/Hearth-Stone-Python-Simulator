from dataclasses import dataclass

@dataclass
class Card():
  attack: int = 2

@dataclass 
class Player():
  deck: list[Card]
  hand: list[Card]
  board: list[Card
  graveyard: list[Card]
  max_health: int= 30  
  health: int = 30


@dataclass
class GameState():
  player_1: Player
  player_2: Player
