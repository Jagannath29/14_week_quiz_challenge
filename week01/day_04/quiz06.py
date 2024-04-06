# String

strint1 = 'HelloWorld!'
strint1[0] = '!'
strint1[13] = '!'

print(strint1)


'''
    Output:
    TypeError: 'str' object does not support item assignment
    You cannot use indices to directly modify an existing string.
    Strings are immutable. 
'''