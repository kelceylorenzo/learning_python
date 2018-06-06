# # # active flag version
flag = True
while flag:
    topping = input("Please enter a topping to add; enter QUIT when you are finished: ")
    if topping.upper() == 'QUIT':
        flag = False
        print("Thank you for ordering!")
    else:
        print("I will add that topping to your pizza.")

# # # break version
while True:
    topping = input("Please enter a topping to add; enter QUIT when you are finished: ")
    if topping.upper() == 'QUIT':
        print("Thank you for ordering!")
        break
    else:
        print("I will add that topping to your pizza.")

# # # conditional version
topping = input("Please enter a topping to add; enter QUIT when you are finished: ")
while topping.upper() != 'QUIT':
        print("I will add that topping to your pizza.")
        topping = input("Please enter a topping to add; enter QUIT when you are finished: ")