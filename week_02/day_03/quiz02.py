# function, list

def get_freq(lst):
    freq={}
    for item in lst:
        freq[item] = freq.get(item, 0) +   1

    return freq


word = ['apple','ball', 'cat','dog', 'dog','cat']
print(get_freq(word))


'''
    The output is
    {'apple': 1, 'ball': 1, 'cat': 2, 'dog': 2}
    get item and count it.
'''