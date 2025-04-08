# creating a udemy class structure 
#parent class

class User:


    def login(self):
        print("login")

    
    def register(self):
        print("register")

    def __instr(self):
        pass



class Student(User):     # student class is a child class for user 
    #super().__init__(price,brand,camera)
    def enroll(self):
        print("enrol")

    def review(self):
        print("Review")
        #super().register()  #-- using super keyword we can call or invoke the methods or constructor of the parent class. u cant access attr
        #super should be the first statement -- it won't work unless it is one 
        

# an object of child class can access everything from a parent class unless private

#method overriding ---- an object of child class , will call the method from the child class only if there is a method with the same name
#in the parent class as well.  --polymorphism 


stu1 = Student()

stu1.login()
stu1.enroll()
stu1.register()
stu1.review()
