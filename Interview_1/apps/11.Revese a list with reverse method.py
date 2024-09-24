# 11.Revese a list with reverse method

# my_list = [10, 20, 70, 40, 50]
# my_list.reverse()
# print(my_list)

def reverse_list(my_list):
    """
    Reverse a list using the reverse method.

    Args:
        my_list (list): The input list

    Returns:
        list: The reversed list
    """
    try:
        if not isinstance(my_list, list):
            raise TypeError("Input must be a list")
        my_list.reverse()
        return my_list

    except TypeError as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


my_list = [1, 2, 3, 4, 5]
result = reverse_list(my_list)
print("Reversed list:", result)