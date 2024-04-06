# for loop, continue

for var in 'Hello how are':
    if var in ['o']:
        continue
    print(var, end='')

'''
    output is 'Hell hw are'
    continue skips the letter if the letter is found
    end = '' prints in the same line
'''