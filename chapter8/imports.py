import cities
cities.describe_city('tokyo', 'japan')

from cities import describe_city
describe_city('barcelona', 'spain')

from cities import describe_city as dc
dc('syndey', 'australia')

import cities as c
c.describe_city('paris', 'france')

from cities import *
describe_city('toronto', 'canada')