# 9. Count the occurrences of an element in a list without using builtIn method.

#
# a = [1,2,2,2,2,2,6,8,8,8,5,5]
# count = 0
# for i in a:
#     if i == 2:
#         count += 1
# print(count)

def count_occurrences(lst, element):
    """
    Count the occurrences of an element in a list without using the count method.

    Args:
        lst (list): The input list
        element: The element to count

    Returns:
        int: The number of occurrences of the element in the list
    """
    try:
        if not isinstance(lst, list):  # edge case: input is not a list
            raise TypeError("Input must be a list")

        count = 0
        for item in lst:
            if item == element:
                count += 1
        return count

    except TypeError as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
result = count_occurrences(my_list, element)
print(f"The element {element} occurs {result} times in the list {my_list}.")



non_list_input = "hello"
result = count_occurrences(non_list_input, element)
print(f"The element {element} occurs {result} times in the list {my_list}.")

# Test with a non-integer element
mixed_list = [1, 2, 'a', 4, 5]
element = 'a'
result = count_occurrences(mixed_list, element)
print(f"The element {element} occurs {result} times in the list {my_list}.")
