rivers = {
    'nile' : 'egypt',
    'mississippi' : 'usa',
    'rhine' : 'germany'
}

for key, value in rivers.items():
    if value == 'usa':
        print('The ' + key.title() + ' runs through ' + value.upper())
    else:
        print('The ' + key.title() + ' runs through ' + value.title())

print('\n')

for river in rivers.keys():
    print(river.title())

print('\n')

for country in rivers.values():
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())
