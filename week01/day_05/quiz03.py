def reset_uname_and_pass():
    uname = input('Enter your name: ')
    password = input('Enter your pass: ')

    is_uname = len(uname) > 0
    is_pass = len(password) > 8

    if all([is_uname, is_pass]):
        print('Reset successfully')

    else:

        print('Please enter valid user name and password: ')

reset_uname_and_pass()

