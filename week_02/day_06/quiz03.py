# set

set1 = (1,5,9)
set2 = (9,6,3)
common = set()

for i in set1:
    if i in set2:
        common.add(i)

print(common)


'''
    The output is: {9}

    takes only common
    
'''