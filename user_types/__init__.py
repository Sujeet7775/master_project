# Correctly define string constants
Admin = 'Admin'
Staff = 'Staff'
Supervisor = 'Supervisor'
Director = 'Director'
Employee = 'Employee'

# Now define the choices list
USER_TYPE_CHOICES = [
    (Admin, 'Admin'),
    (Staff, 'Staff'),
    (Supervisor, 'Supervisor'),
    (Director, 'Director'),
    (Employee, 'Employee'),
]
