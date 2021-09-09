#Parent Class User
class User:
    name = 'David'
    email = 'clutchmandd@gmail.com'
    password = 'pAssW0rd'

    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('Your password or email is incorrect.')


#Child Class Employee
class Employee(User):
    hourly_pay_rate = 35.00
    job_description = 'Developer'
    pin_number = '1234'

    #Same method as Parent Class, but modified for Child Class Employee
    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_pin = input('Enter your pin: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('Your pin or email is incorrect.')


#Child Class Administrator
class Admin(User):
    hourly_pay_rate = 55.00
    job_description = 'Administrator'
    token_id = '857-956'

    #Same method as Parent Class, but modified for Child Class Administrator
    def getLoginInfo(self):
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        token_id = input('Enter your token_id: ')
        if (entry_email == self.email and entry_password == self.password):
            print('Welcome back, {}!'.format(entry_name))
        else:
            print('Your token-id or email is incorrect.')


customer = User()
customer.getLoginInfo()

employee = Employee()
employee.getLoginInfo()

administrator = Admin()
administrator.getLoginInfo()
