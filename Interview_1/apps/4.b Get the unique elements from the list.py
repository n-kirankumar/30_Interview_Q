# 4.b Get the unique elements from the list. i/p [2,2,3,4,4,4,5] output [2,3,4,5]

def remove_duplicates_in_list(my_list):
    """

    :param my_list: takes list with duplicate values
    :return: unique_list
    """
    try:
        unique_list = []
        for i in my_list:
            if i not in unique_list:
                unique_list.append(i)
        return unique_list
    except Exception as e :
        return e

my_list = [2,2,3,4,4,4,5]
print(remove_duplicates_in_list(my_list))