
class Student:
    def __init__(self, name,registration,course):
        self.name = name
        self.registration = registration
        self.course = course
        
    def view_student(self):
        return f"{self.name}, registration number : {self.registration}, is pursuing {self.course} at The Co-operative University of Kenya"
    

class Teacher:
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
    
    def teach_student(self, student, callback):
        print(f"{self.name} is teaching {student.name}")
        
        #call the callback function 
        callback(student)
        
#Create Student
std1 = Student("John","A100","computer science")

#Create Teacher
teacher1 = Teacher("Miss Joy","T002")

#Callback function
def give_assignment(student):
    print(f"{student.name} has been assigned a python assignment")

#Pass the funnction
teacher1.teach_student(std1, give_assignment)
