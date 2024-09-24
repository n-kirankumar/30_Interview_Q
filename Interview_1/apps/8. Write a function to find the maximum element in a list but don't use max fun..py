# 8. Write a function to find the maximum element in a list but don't use max fun.

# a = [1, 2, 3, 4]
#
# for i in range(len(a)):
#     maximum = a[0]
#     if a[i] > maximum:
#         maximum = a[i]
#
# print(maximum)


def find_max(lst):
    """
    Find the maximum element in a list without using the max function.

    Args:
        lst (list): The input list

    Returns:
        int: The maximum element in the list
    """
    try:
        if not lst:  # edge case: empty list
            return None

        max_element = lst[0]  # initialize max_element with the first element
        for element in lst[1:]:  # iterate through the rest of the list
            if element > max_element:
                max_element = element

        return max_element

    except TypeError:
        print("Error: The input list must contain only integers.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

my_list = [3, 1, 4, 10, 2, 6]
result = find_max(my_list)
print("The maximum element in the list is:", result)

# Test with an empty list
empty_list = []
result = find_max(empty_list)
print("The maximum element in the list is:", result)

# Test with a list containing non-integer elements
mixed_list = [1, 2, 'a', 4, 5]
result = find_max(mixed_list)
print("The maximum element in the list is:", result)