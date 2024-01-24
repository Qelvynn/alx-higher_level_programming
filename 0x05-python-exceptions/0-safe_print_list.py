#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    """Prints up to x elements of a list, handling any index errors.

    Args:
        my_list (list, optional): The list to print elements from. Defaults to None.
        x (int, optional): The maximum number of elements of my_list to print. Defaults to 0.

    Returns:
        int: The actual number of elements printed.
    """
    # Initialize the return value to 0
    ret = 0
    # Use an empty list if no list is given
    if my_list is None:
        my_list = []
    # Loop through the indices from 0 to x-1
    for i in range(x):
        try:
            # Print the element at index i, without a newline
            print(my_list[i], end="")
            # Increment the return value by 1
            ret += 1
        except IndexError:
            # Break the loop if the index is out of range
            break
    # Print a newline after the loop
    print()
    # Return the number of elements printed
    return ret
