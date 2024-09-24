# 18.Get the odd numbers from a list - use list comprehensions

# a = [1,2,3,4]
# b = [i for i in a if i %2 != 0]
# print(b)


def get_odd_numbers(numbers):
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        odd_numbers = [num for num in numbers if num % 2 != 0]
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