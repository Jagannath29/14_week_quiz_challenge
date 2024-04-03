# function, if, for loop, modulo operator

def is_odd(numbers):
    lst = []
    for i in numbers:
        if i%2 != 0:
            lst.append(i)

    return lst

n = [1,2,3,4,5,6]
print(is_odd(n))

'''
The output is [1, 3, 5]
'i%2' operator returns the reminder of division.



'''