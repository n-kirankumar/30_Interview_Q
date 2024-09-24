# 22.Remove all occurrences of a 2 from the list i/p [1,2,2,3,3,3,4] o/p [1,3,3,4]

# a = [1,2,2,3,3,3,4]
# b = [i for i in a if i != 2]
# print(b)

def remove_element(numbers, element):
    """

    :param numbers: list
    :param element: int
    :return: list
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        numbers_without_element = [num for num in numbers if num != element]
        return numbers_without_element

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

numbers = [1, 2, 2, 3, 3, 3, 4]
result = remove_element(numbers, 2)
print(result)