# list, comprehension

lst = [11,24,13,115,17,21,5,8]
odd_list = [i**2 for i in lst if i%2!=0 ]
print(odd_list)


''''
    The output is
    [121, 169, 13225, 289, 441, 25]
'''