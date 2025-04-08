# flake8: noqa
class Car:
    """
    A class to represent a car.
    """

    def __init__(self, make, model):
        """
        Initialize the car with make and model and a private attribute price
        """
        self.make = make
        self.model = model
        self.__price = None

    def set_price(self, new_price):
        """
        Set the price of the car
        """
        self.__price = new_price

    def get_price(self):
        """ 
        Return the price of the car
        """
        return self.__price

    def display_info(self):
        """
        Display the make and model of the car.
        """
        print(f'The make of the car is {self.make}')
        print(f'The model of the car is {self.model}')
        print(f'The Price of the car is {self.get_price()}')


class ElectricCar(Car):
    """
    Inherits from the base class -car
    """
    def __init__(self,make,model,battery_capacity):
        """
        Initialze the 
        """

        super().__init__(make,model)
        self.battery_capactiy = battery_capacity




# Creating an object of the Car class.
obj = Car('1991', '2')


obj.set_price(9121)


obj.display_info()

