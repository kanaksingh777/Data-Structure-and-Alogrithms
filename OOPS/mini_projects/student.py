
class Student:

    def __init__(self,name,grades):
        self.name = name 
        self.grades  = {}

    def add_grade(self,subject,mark):
        
    
        self.grades[subject] = mark
    
    def calculate_average(self):
        total_marks = 0
        for k,v in self.grades.items():
            total_len =len(self.grades)
            total_marks +=v
        return total_marks/total_len
        
    def display_grades(self):
        print(self.grades.items())


        
