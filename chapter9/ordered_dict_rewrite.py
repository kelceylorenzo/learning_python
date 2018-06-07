from collections import OrderedDict

glossary = OrderedDict()

glossary['tuple'] = 'An immutable list'
glossary['append'] = 'To add a new element to a list'
glossary['boolean'] = 'A conditional'
glossary['dictionary'] = 'A collection of key-value pairs'
glossary['string'] = 'A series of characters'
glossary['list'] = 'A collection of items in a particular order'
glossary['slice'] = 'A specific group of items in a list'

for key, value in glossary.items():
    print(key.title() + ': ' + value)

# Or

# for word in glossary.keys():
#     print(word.title() + ': ' + glossary[word])
