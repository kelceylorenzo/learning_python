from number_served import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = []
    
    def add_favors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
    
    def show_flavors(self):
        print('The current available flavors are: ')
        for flavor in self.flavors:
            print(flavor)

new_stand = IceCreamStand('Very Good Ice Cream', 'ice cream')
new_stand.add_favors('chocolate', 'vanilla', 'strawberry', 'coffee', 'cookies \'n cream')
new_stand.show_flavors()