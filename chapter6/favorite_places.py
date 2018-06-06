favorite_places = {
    'kelcey' : ['maui', 'tokyo', 'seoul'],
    'jeremiah' : ['tokyo', 'new york', 'yokohama'],
    'peter' : ['neverland', 'corona', 'atlantis']
}

for person in favorite_places.keys():
    print('\n'+person.title() + ':')
    print(favorite_places[person][0].title())
    print(favorite_places[person][1].title())
    print(favorite_places[person][2].title())
