# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return {
            "Name": self.name,
            "Age": self.age
        }

# Derived Class: Student
class Student(Person):
    # Class variable to store all students
    student_list = []

    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []  # List of dictionaries: [{"course_name": "Math", "grade": "A"}, ...]

        # Add to class-level list
        Student.student_list.append(self)

    def add_course(self, course_name, grade):
        self.courses.append({"course_name": course_name, "grade": grade})

    def calculate_gpa(self):
        # Grade to GPA conversion
        grade_points = {
            "A+": 4.0, "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0, "F": 0.0
        }

        total_points = 0
        total_courses = len(self.courses)

        for course in self.courses:
            grade = course["grade"]
            total_points += grade_points.get(grade, 0.0)  # Default to 0.0 if grade not found

        return round(total_points / total_courses, 2) if total_courses > 0 else 0.0

    def get_details(self):
        details = super().get_details()
        details["Student ID"] = self.student_id
        details["Courses"] = self.courses
        details["GPA"] = self.calculate_gpa()
        return details

# Derived Class: Teacher
class Teacher(Person):
    def __init__(self, teacher_id, name, age, subject):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject

    def get_details(self):
        details = super().get_details()
        details["Teacher ID"] = self.teacher_id
        details["Subject"] = self.subject
        return details
  
def load_student(file_name):
    with open(file_name,'r') as file :
        for line in file : 
            print(line)
            print("hi")



file_name = "source.txt"
students = load_student(file_name)