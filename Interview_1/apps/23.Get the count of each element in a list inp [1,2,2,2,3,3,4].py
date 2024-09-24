# 23.Get the count of each element in a list i/p [1,2,2,2,3,3,4] o/p {1:1,2:3,3:2,4:1}

# a = [1,2,2,2,3,3,4]
# b = {}
# for i in a :
#     b[i] = a.count(i)
# print(b)

def count_elements(numbers):
    try:
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of numbers")
        element_counts = {num: numbers.count(num) for num in set(numbers)}
        return element_counts

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


numbers = [1, 2, 2, 2, 3, 3, 4]
result = count_elements(numbers)
print(result)