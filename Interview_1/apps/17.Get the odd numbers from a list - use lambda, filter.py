# 17.Get the odd numbers from a list - use lambda, filter

# a = [1, 2, 3, 4, 5, 6, 7]
# b = list(filter((lambda x : x % 2 != 0),a))
# print(b)

def get_odd_numbers(numbers):
    """
    :param numbers:list
    :return: list with odd numbers
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
        return odd_numbers

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = get_odd_numbers(numbers)
print(odd_numbers)