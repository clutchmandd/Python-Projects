# Creating a Class using the __init__() function
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def myfunc(self):
        print('Hello my name is ' + self.fname + ' ' + self.lname + '.')

# Creating an instance
p1 = Person('David','Dixon',35)
p1.myfunc()
