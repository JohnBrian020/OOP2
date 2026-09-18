class Student:
    def __init__(self, name, registration, course):
        self.name = name
        self.registration = registration
        self.course = course

        # We use _grade because we will control access to it
        self._grade = 0

    def view_student(self):
        return (
            f"{self.name}, registration number: {self.registration}, "
            f"is pursuing {self.course} at "
            f"The Co-operative University of Kenya"
        )
        
    #GETTER
    @property
    def grade(self):
        return self._grade
    
    #SETTERs
    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            print("Grade must be between 0 and 100.")
        else:
            self._grade = new_grade
            
class Teacher:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
        
    def teach_student(self, student, callback):
        print(f"{self.name} is teaching {student.name}")
        # Call the callback function
        callback(student)
        
def give_assignment(student):
    print(f"{student.name} has been assigned a python assignment")
    
std1 = Student("John","S101", "Software Engineering")
std2 = Student("Barack","S110", "Data Science")
std3 = Student("Acey","S102", "Cyber Security")

teacher1 = Teacher("Miss Joy", "T002")
teacher2 = Teacher("Mr Kimende", "T010")

print(std1.view_student())

std1.grade = 85

#Use Getter
print(f"{std1.name}'s grade is {std1.grade}")

#Callback
teacher1.teach_student(std1, give_assignment)

