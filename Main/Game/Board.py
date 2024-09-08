class EventManager:
    def __init__(self):
        self._subscribers = {}

    def register_event(self, event_type, callback):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        if callback not in self._subscribers[event_type]:
            self._subscribers[event_type].append(callback)

    def unregister_event(self, event_type, callback):
        if (
            event_type in self._subscribers
            and callback in self._subscribers[event_type]
        ):
            self._subscribers[event_type].remove(callback)

    def trigger_event(self, event_type, *args, **kwargs):
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                callback(*args, **kwargs)






class Board:
    def __init__(self):
        self.event_manager = EventManager()
        self.players = [Player(), Player()]
        self.current_player = 0

    def end_turn(self):
        self.current_player = 1 - self.current_player
        self.event_manager.trigger_event("turn_end", self.current_player)