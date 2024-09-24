# 13.Get the even numbers from a list - use loop and append

# a = [1, 2, 3, 4, 5, 6]
#
# even_a = []
# for i in a :
#     if i % 2 == 0:
#         even_a.append(i)
# print(even_a)


def even_numbers_from_list(my_list):
    """
    check even number from a given list
    :param my_list: as input to function
    :return: list with even number
    """
    try:
        if not isinstance(my_list, list):
                raise TypeError("Input must be a list")
        even_list = []
        for i in my_list:
            if i % 2 == 0:
                even_list.append(i)
        return even_list

    except TypeError as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

my_list =  [1, 2, 3, 4, 5, 6]
result = even_numbers_from_list(my_list)
print(result)