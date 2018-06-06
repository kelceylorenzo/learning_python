results = {}
active = True

while active:
    name = input('\nName: ')
    place = input('If you could visit one place in the world, where would you go? ')
    
    results[name] = place

    repeat = input('Thank you for taking the survey. Would you like to let another person take the survey? y/n ')

    if repeat == 'n':
        active = False

print('\nResults of the poll:')
for name in results.keys():
    print(name.title())
    print(results[name].title())
print('\nGoodbye.')