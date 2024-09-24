# 20.Get the strs from the list - use list comprehensions
#
# a = [1 ,2 ,'radha','krishna',1.5]
# b = []
# for i in a :
#     if type(i) == str:
#         b.append(i)
# print(b)


def get_strings(mixed_list):
    try:
        if not isinstance(mixed_list, list):
            raise ValueError("Input must be a list")
        strings = [i for i in mixed_list if isinstance(i, str)]
        return strings

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

mixed_list = [1 ,2 ,'radha','krishna',1.5]
strings = get_strings(mixed_list)
print(strings)