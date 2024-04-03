# zip function, for loop

# def zip_function(question, answer):
#     for q, a in zip(question, answer):
#         print(f'what is your {q}, it is {a}')

# zip_function(['age', 'age'], [30, 22])


'''
The output is 
what is your age, it is 30
what is your age, it is 22

Zip efficiently combines data from multiple sequences
ues case: Transposing a matix or creating a dictionary

using the unpacking operator '*' helps with code readibility and flexibility


'''

def zip_function(question, answer):
    for q, a in zip(*question, *answer):
        print(f'what is your {q}, it is {a}')

zip_function(['age', 22], ['age', 50])