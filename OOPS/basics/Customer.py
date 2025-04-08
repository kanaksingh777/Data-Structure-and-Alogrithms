class Customer():

    def __init__(self,name,gender):
        self.name = name 
        self.gender = gender 

    
def greet(customer):
        
    customer.name = "random"  # this shows that we can change the data inside the object 
    print(customer.name)
    if customer.gender =="Male":


            print("hello",customer.name,"Sir")
    else: 
            print("hello",customer.name, "ma'am")





#cust = Customer("kanak")
cust2 = Customer("Kenny","Male")  #call by reference 
greet(cust2)
print(cust2.name)
