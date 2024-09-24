# 30.Merge two lists and sort them in ascending order.

def merge_and_sort(list1, list2):
    """

    :param list1: list
    :param list2: list
    :return: sorted list
    """
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise ValueError("Both inputs must be lists")
        merged_list = list1 + list2
        sorted_list = sorted(merged_list)
        return sorted_list

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


list1 = [3, 1, 4]
list2 = [2, 5, 6]
result = merge_and_sort(list1, list2)
print(result)
