#flake8: noqa
import datetime

class Passport:

    def __init__(self,first_name,last_name,dob,country,exp_date): 
        self.first_name = first_name 
        self.last_name = last_name
        self.dob = dob
        self.country = country 
        self.exp_date = exp_date



    def is_valid(self):
        if self.exp_date > datetime.datetime.now():
            return True
        else :return False 

    def summary(self):
        if self.is_valid() == True:
            valid = "is valid"
        else : valid = "Invalid"
        return f"The passport belongs to {self.name} and is {valid}"
    
    def check_data(self,first_name,last_name,dob,country):
        valid_status = 'valid' if self.isvalid() else 'not valid'
        #match with the passport object

    def stamp(self,country_name):
        count = {}
        if country_name != self.country:
            count[country_name] = count.get(country_name,0) +1

        else: pass
    
    




