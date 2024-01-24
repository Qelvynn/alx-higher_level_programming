#!/usr/bin/python3

def safe_print_integer(num):
    """Prints an integer with f-string and returns a boolean value.

    Args:
        num (int): The integer to print.

    Returns:
        bool: True if the num is an integer and can be printed, False otherwise.
    """
    try:
        # Try to format and print the num as an integer
        print(f"{num:d}")
        # Return True if no exception is raised
        return (True)
    except (TypeError, ValueError):
        # Return False if the num is not an integer or cannot be formatted
        return (False)
