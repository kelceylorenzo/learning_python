active = True

while active :
    value1 = input('value 1: ')
    value2 = input('value 2: ')
    output = ''

    try: 
        output = int(value1) + int(value2)
    except ValueError:
        print('Please only input numbers')
    else: 
        print(output)

        repeat = input('Find another sum? y/n ')
        if repeat.lower() == 'n':
            print('Goodbye.')
            active = False 