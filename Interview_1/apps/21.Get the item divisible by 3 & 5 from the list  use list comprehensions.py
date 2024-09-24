# 21.Get the item divisible by 3 & 5 from the list - use list comprehensions
#
# a = [10, 20, 30, 15, 16]
# b = [i for i in a if i % 3 == 0 and i % 5 == 0]
# print(b)

def get_divisible_by_3_and_5(numbers):
    """

    :param numbers: list
    :return: list
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        divisible_by_3_and_5 = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
        return divisible_by_3_and_5

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 45, 60]
divisible_by_3_and_5 = get_divisible_by_3_and_5(numbers)
print(divisible_by_3_and_5)