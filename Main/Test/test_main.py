from Main.Game.Board import Board




def test_board_event_manager():
    board = Board()

    # Define a callback function to test event triggering
    def on_turn_end(player_index):
        assert player_index == 1

    # Register the callback with the event manager
    board.event_manager.register_event("turn_end", on_turn_end)

    # End the turn to trigger the event
    board.end_turn()

    # Unregister the callback to clean up
    board.event_manager.unregister_event("turn_end", on_turn_end)

# Add more tests as needed