cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

try: 
    with open(cats_file) as cats_file_object:
        cats_content = cats_file_object.read()
    with open(dogs_file) as dogs_file_object:
        dogs_content = dogs_file_object.read()  
except FileNotFoundError:
    print('Sorry, we seemed to have lost those pets. Please try check your file locations/names.')
else:
    print('\nCats:')
    print(cats_content)
    print('\nDogs:')
    print(dogs_content)
