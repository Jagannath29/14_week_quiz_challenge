# Function

def mystery_func(sen):
    letter = sum(c.isalpha() for c in sen)
    sepcial = sum(not c.isalnum() for c in sen)-sen.count(' ')
    num = sum(c.isdigit() for c in sen)

    return f'letter: {letter}, special: {sepcial}, number: {num}'



sentence = 'hello i have 2$ how much $ dou you have, 10?'

print(mystery_func(sentence))

'''
    The output is:
    letter: 27, special: 4, number: 3
'''