my_favorite_foods = ['pizza', 'falafel', 'carrot cake']
friends_favorite_foods = my_favorite_foods[:]

my_favorite_foods.append('cannoli')
friends_favorite_foods.append('ice cream')

print('My favorite foods are: ')
for food in my_favorite_foods:
    print(food)

print('\nMy friend\'s favorite foods are: ')
for food in friends_favorite_foods:
    print(food)