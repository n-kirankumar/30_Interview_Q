# 28.Calculate the product of all items of the list. i/p [1,2,3,4] o/p 24 use - lambda,reduce


import functools


def calculate_product(lst):
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List cannot be empty")
        product = functools.reduce(lambda x, y: x * y, lst)
        return product

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



input_list = [1, 2, 3, 4]
result = calculate_product(input_list)
print(result)