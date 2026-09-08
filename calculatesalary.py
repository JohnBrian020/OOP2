employees = [
    {"name": "John", "salary": 50000},
    {"name": "Mary", "salary": 70000},
    {"name": "Peter", "salary": 60000},
    {"name": "Andrew", "salary": 23000},
    {"name": "Moses", "salary": 13000}
]

def calculate_salaries(employees, calculation):
    results = []
    
    for employee in employees:
        new_salary = calculation(employee["salary"])
        results.append(new_salary)
    return results
#Callback functions

def add_bonus(salary):
    return salary + 10000

def give_raise(salary):
    return salary * 0.10

bonus_salaries = calculate_salaries(employees, add_bonus)
raised_salaries = calculate_salaries(employees, give_raise)

print("With Bonus:", bonus_salaries)
print("With Raise:", raised_salaries)