# zip, iterable, iterator

a = [1,2,3]
b = ['one', 'two', 'three']
x = zip(a, b)
print(list(x))

'''
The output is (3, 'three)
The zip function takes iterables and return iterators, which generates series of tuples containing elements from each iterable. It accepts any types of iterable
including list, sets, tuple, dictionary.
'''