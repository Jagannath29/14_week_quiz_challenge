# function, dictionary

def my_func(dict1, dict2):
    return {**dict1, **dict2}


d1 = {'a':1, 'b': 2}
d2 = {'b':3, 'c':4}
print(my_func(d1,d2))


'''
    The output is
    {'a': 1, 'b': 3, 'c': 4}
    dictionary doesn't take same key but it update with the latest one.
'''