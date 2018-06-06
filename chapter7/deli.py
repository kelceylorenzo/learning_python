sandwich_orders = ['cheesesteak', 'italian beef', 'french dip', 'reuben',
'hamburger', 'club']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('Making sandwich: ' + current_sandwich)

    finished_sandwiches.append(current_sandwich)

print('\nThe following sandwiches have been made: ')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
