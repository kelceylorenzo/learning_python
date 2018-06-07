class User():
    def __init__(self, first_name, last_name, age, location, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.department = department
        self.login_attempts = 0

    def describe_user(self):
        print('First Name: ' + self.first_name)
        print('Last Name: ' + self.last_name)
        print('Age: ' + self.age)
        print('Location ' + self.location)
        print('Department: ' + self.department)

    def greet_user(self):
        print('Hello, ' + self.first_name + ". How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


# new_user = User('hi', 'ho', '99', 'irv', 'iso')
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.increment_login_attempts()
# print(new_user.login_attempts)
# new_user.reset_login_attempts()
# print(new_user.login_attempts)