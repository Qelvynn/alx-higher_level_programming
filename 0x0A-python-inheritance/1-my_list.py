#!/usr/bin/python3
"""Defines inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
