filename = 'programming_poll.txt'

with open(filename, 'a') as file_object:
    active = True
    while active: 
        reason = input('Why do you like programming? ')
        file_object.write(reason + '\n')

        print('\nReason recorded.')
        repeat = input('Would you like to submit another reason? y/n ')

        if repeat.lower() == 'n':
            print('Thank you for participating.')
            active = False

