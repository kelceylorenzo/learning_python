from login_attempts import User
from privileges import Privilege

class Admin(User):
    def __init__(self, first_name, last_name, age, location, department):
        super().__init__(first_name, last_name, age, location, department)
        self.privileges = Privilege()
    
# admin_1 = Admin('a', 'm', 22, 'irv', 'hr')
# admin_1.privileges.show_privileges()
