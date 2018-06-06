favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'mary grace', 'sarah', 'chris', 'edward', 'phil']

for person in people:
    if person in favorite_languages.keys():
        print('Thank you for taking the poll')
    else: 
        print('Please take our favorite languages poll')
