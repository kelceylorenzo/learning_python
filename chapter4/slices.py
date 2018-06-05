animals = ['red panda', 'fennec fox', 'corgi', 'hedgehog', 'russian blue']
print('The first three animals on the list are: ')
for animal in animals[0:3]:
    print(animal)

print('\nThree animals in the middle of the list are: ')
for animal in animals[1:4]:
    print(animal)

print('\nThe last three animals in the list are: ')
for animal in animals[-3:]:
    print(animal)