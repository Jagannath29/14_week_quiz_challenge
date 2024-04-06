# function, loop, sets

def multiply(num):
    total = 1
    for i in num:
        total *= i

    return total

print(multiply({2,1,2,2}))


'''
    The output is 2
    The code uses set and set can only hold unique value i.e 2,1 
'''