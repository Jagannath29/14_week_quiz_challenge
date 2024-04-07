# isinstance() Function

def sum_num(*args):
    total = 0
    for num in args:
        # here isinstance is uses to filter out the classes that aren't int or float
        if isinstance(num, (int, float)):
            total += num

    return total

print(sum_num(1, 'string',2, [], 3.4))


'''
    The output is 6.4
    isinstance(obj, classInfo) is a built-in function that checks if the inputted function is a member of a inputted classInfo(int, string, etc) and then returns 
    True if it is and False if is not.


'''