class User():
    def __init__(self, first, last, age, location, department):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location
        self.department = department

    def describe_user(self):
        print('First Name: ' + self.first_name)
        print('Last Name: ' + self.last_name)
        print('Age: ' + self.age)
        print('Location ' + self.location)
        print('Department: ' + self.department)

    def greet_user(self):
        print('Hello, ' + self.first_name + ". How are you today?")

class Privilege(): 
    def __init__(self):
        self.privileges = ['read', 'write', 'update', 'delete']
    
    def show_privileges(self): 
        print('Current privileges: ')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, location, department):
        super().__init__(first_name, last_name, age, location, department)
        self.privileges = Privilege()
        

# new_user = User('hi', 'ho', '99', 'irv', 'iso')
# new_user.describe_user()
# new_user.greet_user()
