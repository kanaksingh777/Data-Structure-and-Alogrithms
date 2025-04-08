
# flake8: noqa
class Vehicle:

    def __init__(self,make,model):

        self.make = make
        self.model = model
        self.__price = None  #private attribute

    def set_price(self,price):

        self.__price = price

    def get_price(self):
        
        return self.__price

    def display_info(self):

        print(f'The make of the vehicle is{self.make}')
        print(f'The model of the vehicle is{self.model}')
        price_x = self.__price
        print(f'The price of the vehicle is{price_x}')


class Bike(Vehicle):

    def __init__(self,make,model,engine_capacity):
        super().__init__(make,model)
        self.engine_capacity = engine_capacity

    def display_engine_capacity(self):

        print(f'engine capacity of the {self.model} is {self.engine_capacity}')
    
    def display_info(self):
        super().display_info()

        print(f'engine capacity is {self.engine_capacity}')

class Truck(Vehicle):
    
    def __init__(self,make,model,max_load_capacity):
        super().__init__(make,model)
        self.max_load_capacity = max_load_capacity

    def display_load_capacity(self):
        print(f'load capacity of the {self.model} is {self.max_load_capacity}')
    
    def display_info(self):
        super().display_info()

        print(f'engine capacity is {self.max_load_capacity}')



# Create a Bike object
bike = Bike('Yamaha', 'MT-15', 155)
bike.set_price(150000)
bike.display_info()
bike.display_engine_capacity()

# Create a Truck object
truck = Truck('Volvo', 'FMX', 25)
truck.set_price(4000000)
truck.display_info()
truck.display_load_capacity()
