class Restaurant():
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name.title())
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open!')

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, costumers_served):
        self.number_served += costumers_served


# urban_seoul = Restaurant('urban seoul', 'Korean fusion')
# print('Number served: ' + str(urban_seoul.number_served))

# urban_seoul.set_number_served(22)
# print('Number served: ' + str(urban_seoul.number_served))

# urban_seoul.increment_number_served(2)
# print('Number served: ' + str(urban_seoul.number_served))

# urban_seoul.increment_number_served(5)
# print('Number served: ' + str(urban_seoul.number_served))

