# zip

name = ['hen', 'dog', 'cat', 'dog']
age = [11,12,13,14]

combine = list(zip(name, age))

dog_ages = [age for name, age in combine if name == 'dog']

print(dog_ages)


'''
    The output is [12, 14]
'''