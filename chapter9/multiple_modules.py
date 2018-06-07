from users import User
from admin import Admin
from privileges import Privilege

multiple_module_admin = Admin('kelly', 'parker', 30, 'sno', 'hr')
multiple_module_admin.privileges.show_privileges()