# function, tuple

def my_func(tup1, tup2):
    return tuple(set(tup1) & set(tup2))

t1 = (1,2,3,4)
t2 = (3,4,5,6)

print(my_func(t1, t2))



'''
the output is: 
(3,4)
'''