flag = True
while flag:
    topping = input("Please enter a topping to add; enter QUIT when you are finished: ")
    if topping.upper() == 'QUIT':
        flag = False
        print("Thank you for ordering!")
    else:
        print("I will add that topping to your pizza.")