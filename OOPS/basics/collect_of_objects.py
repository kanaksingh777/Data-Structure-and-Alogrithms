class Customer():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        
        print(f"I am {self.name} and i am {self.age} year's old ")

c1 = Customer("kanak",27)
c2 = Customer("Kenny",28)
c3 = Customer("zoi",1)

L = [c1,c2,c3]

# for i in L :
#     print(i.name, i.age)

for i in L:
    i.intro()
