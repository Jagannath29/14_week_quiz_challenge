# list, copy

nested_list = [[1,2], [5, 6]]
nested_list2 = nested_list.copy()

nested_list2[1][0] = 8

print(nested_list)

'''
    The output is [[1, 2], [8, 6]]
'''