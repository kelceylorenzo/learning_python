class Restaurant():
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name.title())
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open!')
