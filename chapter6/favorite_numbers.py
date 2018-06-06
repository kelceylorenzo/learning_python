favorite_numbers = {
    'shiro' : [12, 3, 56,12,7],
    'keith' : [7, 13],
    'hunk' : [22, 39,1230],
    'lance' : [30,66,11],
    'pidge' : [5]
}

for person in favorite_numbers.keys():
    print('\n'+person.title() + ':')
    for number in favorite_numbers[person]:
        print(number)
