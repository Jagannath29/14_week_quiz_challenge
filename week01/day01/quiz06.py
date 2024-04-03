mystring = 'Python is fun lets learn together'
counter = 0
for i in range(len(mystring)):
    if mystring[i] == 'e':
        counter +=1
print(counter)


'''
the output is 4 in this string.

Note: you can itrate by the index of sequences using range(len(mystring))
'''