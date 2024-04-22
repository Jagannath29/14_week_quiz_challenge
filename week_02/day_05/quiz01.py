# function 

def check_item(seq, item):
    if item in seq:
        return f'{item} is in {seq}'
    
    else:
        return f'{item} not in {seq}' 
my_tupel = (1,4,5,6,3)
print(check_item(my_tupel, 5))


'''
    The output is:
    5 is in (1, 4, 5, 6, 3)
'''