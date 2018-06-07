def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print(magician.title())

def make_great(list_of_magicians):
    great_magicians = []
    for magician in list_of_magicians:
        great_magicians.append(magician.title() + ' the great')
    return great_magicians

magicians = ['houdini', 'copperfield', 'angel', 'blaine']
unchanged_magicians = make_great(magicians)

show_magicians(magicians)
show_magicians(unchanged_magicians)