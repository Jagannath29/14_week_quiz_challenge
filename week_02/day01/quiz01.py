# dictionary

dict1 = {'mango': 1.1, 'banana': 12, 'apple': 3.2}
updates = [('banana', 5), ('apple', 3), ('grapes', 11)]
dict1.update(updates)
print(dict1)

'''
    The outpt is {'mango': 1.1, 'banana': 5, 'apple': 3, 'grapes': 11}

    if you want to merge you can do this merge_dice = {**duct1, **updates}
'''