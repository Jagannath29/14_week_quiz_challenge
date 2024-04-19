# set, function, level-2

def func(lists):
    sets = [set(lst) for lst in lists]
    union = set().union(*sets)

    return len(union)


lst = [[1,4,7], [2,1,8],[3,6,9]]
print(func(lst))

'''
    The output is: 8
    lsit convert into set. set doesn't take duplicate values
'''