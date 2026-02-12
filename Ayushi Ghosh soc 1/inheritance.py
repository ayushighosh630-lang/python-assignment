class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Employee.__init__(self, name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)

# create object
m1 = Manager("Ayushi", 25, "E101", 50000, "IT")
m1.show_details()
