# set, loop, function

def my_fun(my_list):
    seen = set()
    duplicate = set()

    for item in my_list:
        if item in seen:
            duplicate.add(item)
        seen.add(item)

    return list(duplicate)


lst = [1,2,2,3,4,7,7,8,1,9,10,2]
print(my_fun(lst))


'''
    returns only the duplicate
    The output is:
    [1, 2, 3, 4, 7, 8, 9, 10]
'''