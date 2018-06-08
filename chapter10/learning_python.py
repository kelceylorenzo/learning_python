filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print('Reading file as a whole')
    print(contents)

with open(filename) as file_object:
    print('\nReading file by line')
    for line in file_object:
        print(line)

with open(filename) as file_object:
    print('\nReading file by storing as list')
    lines = file_object.readlines()
output = ''
for line in lines:
    output += line.strip()
print(output)