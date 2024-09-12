"""testing module"""


def my_function(x: int) -> int:
    """
    Returns:
        int
    """
    return x


def test_my_function() -> None:
    """
    Returns:
        None
    """
    # Example test case
    input_value = 5
    expected_output = 25  # Assuming my_function squares the input
    assert (
        my_function(input_value) == expected_output
    ), f"Expected {expected_output}, but got {my_function(input_value)}"
