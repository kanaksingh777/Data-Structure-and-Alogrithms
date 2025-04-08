# flake8: noqa

class Employee:
    employee_count = 0

    def __init__(self, name, age, base_salary):
        self.name = name
        self.age = age
        self.base_salary = base_salary
        Employee.employee_count += 1

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, age, base_salary, bonus):
        super().__init__(name, age, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Developer(Employee):
    def __init__(self, name, age, base_salary):
        super().__init__(name, age, base_salary)
        self.projects = []

    def calculate_salary(self):
        return super().calculate_salary() + len(self.projects) * 500


# Utility function to read employees from a file
def read_employees_from_file(file_path):
    employees = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == "Employee":
                employees.append(Employee(data[1], int(data[2]), int(data[3])))
            elif data[0] == "Manager":
                employees.append(Manager(data[1], int(data[2]), int(data[3]), int(data[4])))
            elif data[0] == "Developer":
                dev = Developer(data[1], int(data[2]), int(data[3]))
                dev.projects = data[4].split(';') if len(data) > 4 else []
                employees.append(dev)
    return employees


# Function to generate report
def generate_report(employees):
    report = {"Employee": [], "Manager": [], "Developer": []}
    for emp in employees:
        if isinstance(emp, Manager):
            report["Manager"].append(emp.name)
        elif isinstance(emp, Developer):
            report["Developer"].append(emp.name)
        else:
            report["Employee"].append(emp.name)
    return report


# Main Execution
if __name__ == "__main__":
    # Sample employee data
    sample_data = """\
Employee,John,30,50000
Manager,Susan,45,80000,10000
Developer,Alex,28,60000,Project1;Project2
"""

    # Write sample data to a file
    with open("employees.txt", "w") as file:
        file.write(sample_data)

    # Read employees from the file
    employees = read_employees_from_file("employees.txt")

    # Generate and print report
    report = generate_report(employees)
    print("Employee Report:", report)

    # Print salaries of all employees
    for emp in employees:
        print(f"{emp.name} earns {emp.calculate_salary()} as salary.")
