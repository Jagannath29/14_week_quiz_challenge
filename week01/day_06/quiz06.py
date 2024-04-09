# dictionary key, value

names = {'John': 20, 'Micheal': 23, 'Thomas': 14, 'Anthony': 25}

for name, age in names.items():
    print(f'{name} is {age}')


'''
    The output is: 
        John is 20
        Micheal is 23
        Thomas is 14
        Anthony is 25

        note:
            item() method allows us to itrate over dictionary to access both the keys and the values
'''