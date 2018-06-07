def city_county(city, country):
    return  '"' + city.title() + ', ' + country.title() + '"'

location = city_county('los angeles', 'usa')
print(location)

location = city_county('barcelona', 'spain')
print(location)

location = city_county('paris', 'france')
print(location)