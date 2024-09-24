# 14.Get the even numbers from a list - use lambda, filter

# def even_numbers_from_list_lambda_filter():

# my_list = [1, 2, 3, 4, 5, 6]
# x = filter((lambda x : x % 2 == 0 ),my_list)
# print(list(x))

def even_numbers_from_list_lambda_filter(my_list):
    try :
        if not isinstance(my_list,list):
            raise TypeError('input must be list ')
        even_list = list(filter((lambda x : x % 2 ==0 ),my_list))
        return even_list

    except TypeError as e :
        print(f'error : {e}')
        return None

    except Exception as e :
        print(f"unexpected error occured : {e}")
        return None


my_list = [1, 2, 3, 4, 5 ]
result = even_numbers_from_list_lambda_filter(my_list)
print(result)

