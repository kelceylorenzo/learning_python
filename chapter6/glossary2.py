glossary = {
    'tuple': 'An immutable list',
    'append' : 'To add a new element to a list',
    'boolean' : 'A conditional',
    'dictionary' : 'A collection of key-value pairs',
    'string' : 'A series of characters',
    'list' : 'A collection of items in a particular order',
    'slice' : 'A specific group of items in a list'
}

for key, value in glossary.items():
    print(key.title() + ': ' + value)

# Or

for word in glossary.keys():
    print(word.title() + ': ' + glossary[word])
