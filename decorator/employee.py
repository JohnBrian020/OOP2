class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self._salary = salary #private attribute
    
    @property
    def salary(self):
        return self._salary
    
    @salary.getter
    def salary(self, value):
        if value < 0:
            raise ValueError("salary can't be negative")
        self._salary = value
        
emp1 = Employee("Alice", 20000)
print(emp1._salary) 