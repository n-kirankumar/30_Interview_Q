# 15.Get the even numbers from a list - use list comprehensions!


# my_list = [1, 2, 3, 4, 5 ]
# even_list = [i for i in my_list if i % 2 == 0]
# print(even_list)


def get_even_numbers(numbers):
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        even_numbers = [num for num in numbers if num % 2 == 0]
        return even_numbers

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)