# filter

def is_even(numbers):
    return numbers % 2 == 0

num = [1,2,3,4,5,6,7,8,9,10,10,12,13]
even_nums = list(filter(is_even, num))
print(even_nums)


'''
    The filter () function can filter items from an iterable based on a function that returns a boolean value.
'''