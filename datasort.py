students = [
    {"name": "Brian", "age": 22},
    {"name": "Alice", "age": 20},
    {"name": "John", "age": 25}
]
    
def get_age(student):
    return student["age"]

sorted_student = sorted(students, key=get_age)
print(sorted_student)