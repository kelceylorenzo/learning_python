sandwich_orders = ['cheesesteak', 'pastrami', 'italian beef', 'french dip', 'pastrami', 'reuben', 'pastrami','hamburger', 'club']
finished_sandwiches = []

print('The deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('Making sandwich: ' + current_sandwich)

    finished_sandwiches.append(current_sandwich)

print('\nThe following sandwiches have been made: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())