#flake8: noqa

class Person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id 

    def get_details(self):
        return {"Name":{self.name}, "Age":{self.age}, "ID": {self.id} }
    




    

class Student(Person):
    def __init__(self,name,age,id,grade):
        super().__init__(name,age,id)
        self.grade = grade 
        self.subjects = {}

    def get_details(self):
        hashmap =super.get_details()
        return hashmap.update({"grade":{self.grade},"subjects":{self.subjects}})


    def calculate_average(self):
        total_marks = 0
        total_subjects = len(self.subjects)
        for k,v in self.subjects.items():
            total_marks += v
        average = total_marks /total_subjects
        return average 

    
    def add_subject(self,subject_name,marks):
       
        self.subjects[subject_name]=marks


class Teacher(Person):
    def __init__(self,name,age,id,specialization):
        super().__init__(name,age,id)
        self.specialization = specialization
        self.class_assigned = []

    def get_details(self):
        hashmap =super.get_details()
        return hashmap.update({"specialization":{self.specialization},"class_assigned":{self.class_assigned}})

    def assign_class(self):
        pass #your question is wrong here it mentioning to refer the class Class before defining it 

        


class Class:
    def __init__(self,class_name):
        self.class_name = class_name
        self.student = []
        self.teacher = None

    def add_student(self,student:Student):

        self.student.append(student)

    def set_teacher(self,teacher:Teacher):
        self.teacher =Teacher
    
    def get_class_details(self):
        return {"class_name":{self.class_name},"teacher_name" :{self.teacher},"student_list":{self.student}}
    


class School:
    def __init__(self,school_name):
        self.school_name = school_name
        self.classes = {}

    def add_class(self,c_1:Class):
        self.clas
    






