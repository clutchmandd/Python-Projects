from abc import ABC, abstractmethod
class car(ABC):
    def price(self, amount):
        print("The retial price of this car is: ",amount)

    # this function will pass in an argument, but it won't know how or what kind of data it will be
    @abstractmethod
    def creditLimit(self, amount):
        pass


class financing(car):
    # here I define how to implement the creditLimit function from its parent class
    def creditLimit(self, amount):
        print("Your credit limit of {} allows you to purchase this vehicle!".format(amount))


obj = financing()
obj.price("$30,000.00")
obj.creditLimit("30,000.00")
