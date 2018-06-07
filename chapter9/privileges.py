class Privilege: 
    def __init__(self):
        self.privileges = ['read', 'write', 'update', 'delete']
    
    def show_privileges(self): 
        print('Current privileges: ')
        for privilege in self.privileges:
            print(privilege)