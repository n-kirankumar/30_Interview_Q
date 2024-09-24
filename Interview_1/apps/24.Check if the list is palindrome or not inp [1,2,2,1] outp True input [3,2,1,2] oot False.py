# 24.Check if the list is palindrome or not i/p [1,2,2,1] o/p True i/p:[3,2,1,2] o/p:False


def is_palindrome(lst):
    """
    to check list is palindrome or not
    :param lst: list
    :return: boolean
    """
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        return lst == lst[::-1]

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Test cases
print(is_palindrome([1, 2, 2, 1]))
print(is_palindrome([3, 2, 1, 2]))