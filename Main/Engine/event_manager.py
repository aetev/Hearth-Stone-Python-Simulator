"""
module: event_manager.py
"""


class EManage:
    """
    Observer pattern implementation for event management.
    """

    def __init__(self):
        self._subscribers = {}

    def register_event(self, event_type, callback):
        """
        Registers a callback function to be invoked when a specific event type occurs.

        Args:
            event_type (str): The type of event to subscribe to.
            callback (Callable): The function to be called when the event occurs.

        Returns:
            None
        """

        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        if callback not in self._subscribers[event_type]:
            self._subscribers[event_type].append(callback)

    def unregister_event(self, event_type, callback):
        """
        Unregisters a callback function from a specific event type.

        Args:
            event_type (str): The type of the event to unregister from.
            callback (callable): The callback function to remove from the event subscribers.

        """
        if (
            event_type in self._subscribers
            and callback in self._subscribers[event_type]
        ):
            self._subscribers[event_type].remove(callback)

    def trigger_event(self, event_type, *args, **kwargs):
        """
        Triggers an event of the specified type, invoking all subscribed callbacks.

        Args:
            event_type (str): The type of event to trigger.
            *args: Variable length argument list to pass to the callbacks.
            **kwargs: Arbitrary keyword arguments to pass to the callbacks.

        Raises:
            KeyError: If the event_type is not found in the subscribers list.
        """
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                callback(*args, **kwargs)
