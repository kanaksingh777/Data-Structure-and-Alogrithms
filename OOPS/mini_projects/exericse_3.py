#understanding pythonic functions in python


# flake8: noqa
class Temperature:
    def __init__(self):
        self.__celsius =None

    

    @property
    def  celsius(self): 

        return self.__celsius
    

    @celsius.setter
    def celsius(self,temp):
        if temp  < -273.5 :
            raise ValueError("can't set a value below zero")
        self.__celsius = temp

    
    def to_fahrenheit(self):
        temp_in_f = (self.__celsius * 1.8) +32
        return temp_in_f
        


temp = Temperature()
temp.celsius = 25

print(f"Temperature in Celsius: {temp.celsius}")  
print(f"Temperature in Fahrenheit: {temp.to_fahrenheit()}")  
try:
    temp.celsius = -300  # Should raise ValueError
except ValueError as e:
    print(e) 