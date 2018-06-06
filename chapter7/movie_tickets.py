active = True

while active:
    print('Enter your age to see how much your ticket will cost. When you are done, enter QUIT.')
    age = input('What is your age? ')
    if age.upper() == 'QUIT':
        active = False
        print('Thank you!')
    elif int(age) < 3:
        print('Your ticket is FREE')
    elif int(age) <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')