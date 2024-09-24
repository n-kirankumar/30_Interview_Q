#
# 4. How to Remove Duplicates From a List in Python.  i/p [2,2,3,4,4,4,5] output [2,3,4,5]


def remove_duplicates_in_list(my_list):
    """

    :param my_list: contains duplicates
    :return: a list with unique values
    """
    try:
        unique_list = list(set(my_list))
        return unique_list
    except Exception as e :
        return e

my_list = [2,2,3,4,4,4,5,]
print(remove_duplicates_in_list(my_list))