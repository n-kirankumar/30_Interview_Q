# 19.Add 3 to the each item of a list - i/p [2,3,4,5] o/p [5,6,7,8]

#
# a = [1,2,3,4]
# b = []
# for i in a :
#     b.append(i+10)
# print(b)

def add_to_each(numbers, value):
    """

    :param numbers: list
    :param value: int
    :return: list
    """
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        result = [num + value for num in numbers]
        return result

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

numbers = [2, 3, 4, 5,]
result = add_to_each(numbers, 3)
print(result)