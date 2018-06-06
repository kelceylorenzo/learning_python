cities = {
    'tokyo': {
        'country': 'japan', 
        'population': '9.273 million',
        'fact': ' is the largest metropolitan area in the world'
    },
    'seoul': {
        'country': 'south korea',
        'population': '9.86 million',
        'fact': ' is bordered by eight mountains'
    },
    'beijing': {
        'country': 'china',
        'population': '21.71 million',
        'fact': ' is one the bicycle capitals of the world'
    }
    }

for city in cities.keys():
    print('\n' + city.title())
    print(cities[city]['country'].title())
    print(cities[city]['population'])
    print(city.title() + cities[city]['fact'])