# function

def find_repeat_num(number):
    unique_num = set(number)
    repeat_num = [num for num in unique_num if number.count(num)>1]

    return repeat_num


num = [2,4,5,7,1,2,8,4]
print(f'The repeated number are: {find_repeat_num(num)}')


'''
    The output is:
    The repeated number are: [2, 4]

'''