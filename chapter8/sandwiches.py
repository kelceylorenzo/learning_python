def take_order(bread, meat, *toppings):
    print('\nBread: ' + bread)
    print('Meat: ' + meat)
    print('Toppings: ')
    for topping in toppings:
        print('- ' + topping)

take_order('wheat', 'turkey', 'olives', 'lettuce', 'american cheese')
take_order('white', 'ham', 'olives', 'lettuce', 'bell peppers', 'salt & pepper')
take_order('italian herb & cheese', 'turkey', 'cheese')