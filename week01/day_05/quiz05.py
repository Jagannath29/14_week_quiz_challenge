# enumerate

def choose_item(items):
    for i, item in enumerate(items, start=1):
        # print(f'{i}:{item}')
        print(i, item)

    choice = int(input('Select the item number: '))
    return items[choice-1] # i choice is 1 the 1-1 is 0 i.e apple in this case



ite = ['apple','ball','cat','dog','car']
select = choose_item(ite)
print(f'You select {select}')


'''
    enumerate(iterable, start=1) method returns an iterator that contains pair of items within the iterable and its index value.
    create dictionary object with a ready made key:value pair.

'''