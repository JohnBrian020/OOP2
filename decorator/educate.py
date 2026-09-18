class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self._grade = grade
        
    @decorator 
    def grade(self):
        return self._grade
     
    @grade.setter
    def new_grade(self, value):
        if grade < 0 or grade > 100:
            raise ValueError(f"Grade must be between 0 and 100")
        self._grade = value
        
std1 = Student("John","Software Engineer",67)
print(std1._grade)