#!/usr/bin/python3

def safe_print_list_integers(num_list=None, x=0):
    """Prints the first x elements of a list that are integers and returns the number of elements printed.

    Args:
        num_list (list, optional): The list to print elements from. Defaults to None.
        x (int, optional): The maximum number of elements of num_list to print. Defaults to 0.

    Returns:
        int: The number of elements printed.
    """
    # Initialize the return value to 0
    ret = 0
    # Use an empty list if no list is given
    if num_list is None:
        num_list = []
    # Loop through the indices from 0 to x-1
    for i in range(x):
        try:
            # Try to format and print the element at index i as an integer, without a newline
            print(f"{num_list[i]:d}", end="")
            # Increment the return value by 1
            ret += 1
        except (ValueError, TypeError):
            # Skip the element if it is not an integer or cannot be formatted
            continue
    # Print a newline after the loop
    print()
    # Return the number of elements printed
    return ret
