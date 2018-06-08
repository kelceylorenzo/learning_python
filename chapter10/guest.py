filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest = input("Name: ")
    file_object.write(guest)