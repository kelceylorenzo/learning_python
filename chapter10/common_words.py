filename = 'passage.txt'

with open(filename) as file_object:
    content = file_object.readline()
    print(content.lower().count('the'))