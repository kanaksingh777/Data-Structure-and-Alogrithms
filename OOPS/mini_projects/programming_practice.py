# flake8: noqa
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self,animal):
        self.animals.append(animal)
    
    def remove_animal(self,animal):
        self.animals.remove(animal)

    def list_animals(self):
        return self.animals
    
    def total_feet(self):
        feet = 0
        for animal in self.animals:
            feet += animal.get_feet()

        return feet
    
    def count_four_legged(self):
        count = 0
        for animal in self.animals:
            if animal.get_feet() == 4:
                count +=1
        return count


class Animal(Zoo):

    def __init__(self,name,species):
        self.name = name
        self.species = species


    def make_sound(self0):
        return "Animal Sound"
    
    def __str__(self): # magic method
        return self.name  + "is a " +self.species

    def get_feet(self):
        return 4


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

        

    def make_sound(self):
        return "Roar!"
    
class Parrot(Animal):
    def __init__(self,name):
        super().__init__(name,"Parrot")

    def make_sound(self):
        return "Squawk !"
    
    def get_feet(self):
        return 2
    
     


lion1 = Lion("larry")
print(lion1.make_sound())

print(lion1)

 