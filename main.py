# Taking user input boolean (True/False) values in Python

user_input = ''

while True:
    user_input = input('Subscribe to newsletter? True / False: ')

    if user_input.capitalize() == 'True':
        print('The user typed in True')
        break
    elif user_input.capitalize() == 'False':
        print('The user typed in False')
        break

    else:
        print('Enter True or False')
        continue