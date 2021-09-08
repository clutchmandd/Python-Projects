# Parent Class
class User:
    name = ''
    email = ''
    password = ''
    acount_number = 0

# Child 1 Class
class Employee(User):
    hourly_pay_rate = 35.00
    job_description = 'Developer'


# Child 2 Class
class Customer(User):
    address = ''
    tax_exempt = True
