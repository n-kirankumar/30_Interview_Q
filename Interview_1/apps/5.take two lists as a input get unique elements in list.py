# 5. Write a function to take two lists as a input and get unique elements in list



def from_two_lists_get_unique_list(list_1,list_2):
    """
    this function will take two lists as input and will return unique_list contains unique
    elements in both the lists

    :param list_1:
    :param list_2:
    :return: unique list
    """
    try:
        unique_list = set(list_1) & set(list_2)
        return list(unique_list)
    except Exception as e :
        return e


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 9, 2, 10]
print(from_two_lists_get_unique_list(list_1,list_2))

