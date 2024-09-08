from EventManager import EManage
from Player import Player


class Board:
    def __init__(self):
        self.event_manager = EManage()
        self.players = [Player(), Player()]
        self.current_player = 0

    def end_turn(self):
        self.current_player = 1 - self.current_player
        self.event_manager.trigger_event("turn_end", self.current_player)