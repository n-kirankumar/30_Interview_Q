# 7. For given list get the sum of all integers without using builtin functions?


def sum_of_integers(lst):
    """
    Returns the sum of all integers in a list without using built-in functions.

    Args:
        lst (list): The input list containing integers and other elements.

    Returns:
        int: The sum of all integers in the list.

    Raises:
        TypeError: If the input is not a list.
    """
    try:
        total = 0
        for element in lst:
            if isinstance(element, int):
                total += element
        return total
    except TypeError:
        return "Error: Input must be a list."
    except Exception as e:
        return f"An error occurred: {e}"

lst = [1, 2, 3, 4, 5, 'a', 'b', 6, 7, 8]
result = sum_of_integers(lst)
print(result)