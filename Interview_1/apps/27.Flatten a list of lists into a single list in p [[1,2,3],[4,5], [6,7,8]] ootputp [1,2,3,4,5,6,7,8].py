# 27.Flatten a list of lists into a single list. i/p [[1,2,3],[4,5], [6,7,8]] o/p [1,2,3,4,5,6,7,8]


def flatten_list(lst):
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        flattened_list = [item for sublist in lst for item in sublist]
        return flattened_list

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Test case
input_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
result = flatten_list(input_list)
print(result)