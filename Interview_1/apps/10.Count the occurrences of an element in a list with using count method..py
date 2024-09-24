# 10.Count the occurrences of an element in a list with using count method.
#
# a = [10, 10, 10, 50, 80]
# print(a.count(10))


# def count_no_of_occurances_in_list(my_list, element):
#     try :
#         result = my_list.count(element)
#         return result
#     except Exception as e:
#         print(f"error occured as {e}")
#         return None
#
# my_list = [10, 10, 20, 50, 80]
# element = 10
# print(count_no_of_occurances_in_list(my_list, element))

def count_occurrences(lst, element):
    """
    Count the occurrences of an element in a list using the count method.

    Args:
        lst (list): The input list
        element: The element to count

    Returns:
        int: The number of occurrences of the element in the list
    """
    try:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        return lst.count(element)

    except TypeError as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
result = count_occurrences(my_list, element)
print(f"The element {element} occurs {result} times in the list {my_list}")