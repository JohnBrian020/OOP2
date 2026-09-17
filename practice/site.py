class Employee:
    def __init__(self, name, empno, department):
        self.name = name
        self.empno = empno
        self.department = department
    def view_employee(self):
        print(f"{self.name}, employee no {self.empno} is on the {self.department} department")
        
class Manager:
    def __init__(self,name):
        self.name = name
    def manage(self, employee, callback):
        print(f"{employee.name} is managed by {self.name}")
        #calling the callback function
        callback(employee)
        
emp1 = Employee("John","E101","IT")
emp2 = Employee("Gitwari","E201","Transport")

manager = Manager("Mr.Waweru")

#Callback function      
def give_salary(employee):
    print(f"{employee.name} has been assigned their salary")

#Passing the function
manager.manage(emp1, give_salary)
        
    