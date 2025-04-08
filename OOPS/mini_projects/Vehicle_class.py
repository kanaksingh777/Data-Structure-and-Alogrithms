# flake8: noqa
class Vehicle:
    color = "white"
    def __init__(self,name,max_speed,capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity= capacity
        
    
    # def seating_capacity(self, capacity):
    #     return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        return self.capacity *100
    
class Bus(Vehicle):
   
    
    def fare(self):
        total_fare = super().fare()
        maintainence_charge = 0.1 * total_fare
        final_amount = total_fare + maintainence_charge
        return final_amount 





    
school_bus = Bus("School Volva",12,50)
print("Total fare of bus is :",school_bus.fare())
print(type(school_bus))
print(isinstance(school_bus, Vehicle))



