# 22.Check if all elements in the list are positive

# a = [10,20,30,-5,-6,-8]

def check_all_positive(numbers):
    """

    :param numbers:lists
    :return: boolean
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")

        all_positive = all(num > 0 for num in numbers)
        return all_positive

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


numbers = [1, 2, 3, 4, 5]
result = check_all_positive(numbers)
print(result)