# Lambda function

    # without lambda

def is_even(numbers):
    return numbers % 2 == 0

num = [1,2,3,4,5,6,7,8,9,10,10,12,13]
even_nums = list(filter(is_even, num))
print(even_nums)


# With lambda


num1 = [1,2,3,4,5,6,7,8,9,10,10,12,13]
even_num = list(filter(lambda x: x%2==0, num1 ))
print(even_num)


'''
    The output is same for both code i.e [2, 4, 6, 8, 10, 10, 12]

        Keeps the function code short and simple
        It'a main purpose is to import code readability and simplicity
        
'''