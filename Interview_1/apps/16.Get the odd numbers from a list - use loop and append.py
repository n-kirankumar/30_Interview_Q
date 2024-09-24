# 16.Get the odd numbers from a list - use loop and append

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = []
#
# for num in numbers:
#     if num % 2 != 0:
#         odd_numbers.append(num)
# print(odd_numbers)

def get_odd_numbers(numbers):
    """

    :param numbers: takes list
    :return: odd number loist
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")

        odd_numbers = []
        for num in numbers:
            if num % 2 != 0:
                odd_numbers.append(num)
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