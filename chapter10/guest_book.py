filename = 'guest_book.txt'

with open(filename, 'a') as file_object: 
    active = True
    while active:
        guest = input('\nAdd your name to our Guest Book: ')
        file_object.write(guest + '\n')
        print('\nWelcome, ' + guest.title() + '!')
        
        add_another = input('Would you like to add another guest to the Guest Book? y/n ')
        if add_another.lower() == 'n':
            print('\nThank you for visiting!')
            active = False
