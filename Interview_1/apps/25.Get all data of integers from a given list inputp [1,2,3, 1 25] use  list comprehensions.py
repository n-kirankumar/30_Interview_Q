# 25.Get all data of integers from a given list i/p [1,2,3,"india", {1: 25}] use - list comprehensions

def get_integers(lst):
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        integers = [x for x in lst if isinstance(x, int)]
        return integers

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


input_list = [1, 2, 3, "india", {1: 25}]
result = get_integers(input_list)
print(result)