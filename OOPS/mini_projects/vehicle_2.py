class Vehicle:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


    def display_info(self):
        
        """ this method prints the details of the vehicle class"""

        return f"The make of the car is {self. make} , model : {self.model}and year is {self.year}"

class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        super().__init__(make,model,year)
        self.doors = doors

    def display_info(self):
        return f" The make of the car is {self. make} , model : {self.model}and year is {self.year} 
            and it has {self.doors} doors"
    



