# 6. Write a function to take two lists as a input and get unique elements in list in decending order

def unique_elements_from_two_lists(list1, list2):
    try:
        # Convert each list to a set to remove duplicates
        set1 = set(list1)
        set2 = set(list2)

        # Find unique elements in both sets
        unique_elements = set1.union(set2)

        # Convert the set back to a list and sort it in descending order
        sorted_unique_elements = sorted(list(unique_elements), reverse=True)

        return sorted_unique_elements
    except TypeError:
        return "Error: Input lists must contain only hashable elements."
    except Exception as e:
        return f"An error occurred: {e}"
list1 = [1, 2, 3, 2, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = unique_elements_from_two_lists(list1, list2)
print(result)
