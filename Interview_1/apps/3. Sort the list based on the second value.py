"""
3. Sort the list based on the second value of a tuple in a list
input ->[(2,1), (3,0),(5,2)]
Output # [(3,0), (2,1),(5,2)]

"""

input_list = [(2, 1), (3, 0), (5, 2)]

# Sorting the list based on the second value of the tuples
sorted_list = sorted(input_list, key=lambda x: x[1])

# Output the sorted list
print(sorted_list)


"""
def sort_tuples_by_second_value(tuples_list):
    ""
    Sorts a list of tuples based on the second element of each tuple.

    Args:
        tuples_list (list of tuples): A list where each element is a tuple.

    Returns:
        list of tuples: A sorted list of tuples based on the second value.

    Raises:
        TypeError: If the input is not a list or contains non-tuple elements.
        IndexError: If any tuple does not contain at least two elements.
    ""
    try:
        # Check if the input is a list
        if not isinstance(tuples_list, list):
            raise TypeError("Input must be a list of tuples.")

        # Check if all elements are tuples and contain at least two elements
        for item in tuples_list:
            if not isinstance(item, tuple):
                raise TypeError("All elements in the list must be tuples.")
            if len(item) < 2:
                raise IndexError("Each tuple must contain at least two elements.")

        # Sorting the list based on the second value of the tuples
        sorted_list = sorted(tuples_list, key=lambda x: x[1])
        return sorted_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
input_list = [(2, 1), (3, 0), (5, 2)]
result = sort_tuples_by_second_value(input_list)
print(result) 

"""