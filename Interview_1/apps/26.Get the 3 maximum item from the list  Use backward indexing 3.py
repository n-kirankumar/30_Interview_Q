# 26.Get the 3 maximum item from the list - Use backward indexing -3

def get_max_items(lst):
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        if len(lst) < 3:
            raise ValueError("List must have at least 3 elements")
        sorted_lst = sorted(lst, reverse=True)
        max_items = sorted_lst[:3]
        return max_items

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_max_items(input_list)
print(result)