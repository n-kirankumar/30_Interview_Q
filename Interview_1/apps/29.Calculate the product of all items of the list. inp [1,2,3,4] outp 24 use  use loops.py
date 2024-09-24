# 29.Calculate the product of all items of the list. i/p [1,2,3,4] o/p 24 use - use loops


def calculate_product(lst):
    """

    :param lst: list
    :return: integer
    """
    try:
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List cannot be empty")
        product = 1
        for item in lst:
            product *= item
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