# exception, handling error

def find_item(item, my_list):
    try:
        my_list.index(item)
        print(f'{item} found in the list')
    except:
        print(f'{item} not found in the list')

name = ['Jerry', 'Tom', 'Bull', 'henry']
find_item('James', name)


'''
    The output is: James not found in the list

    Things you want to know about Try-Except
            Handling errors and exceptions gracefully in your code.
            Avoiding unexpected crashes and termination of your program
            Provide informati messages to users.
'''