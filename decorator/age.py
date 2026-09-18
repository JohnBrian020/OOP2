class Patient:
    def __init__(self, name, patno, ward, age):
        self.name = name
        self.patno = patno
        self.ward = ward
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print("Age cannot be negative.")
        else:
            self._age = new_age

    def view_patient(self):
        print(f"{self.name}, patient no: {self.patno}, is at ward {self.ward}, age {self.age}")


class Doctor:
    def __init__(self, name):
        self.name = name

    def view_doctor(self, patient, callback):
        print(f"{patient.name} is assigned to {self.name}")

        # Callback
        callback(patient, self)


def treatment(patient, doctor):
    print(f"{patient.name} has been attended to by {doctor.name}.")


# Create objects
ptn1 = Patient("Kamau", "P101", "Menengai", 25)
doctor = Doctor("Mr Glen")

# View patient
ptn1.view_patient()

# Get age using property
print(ptn1.age)

# Change age using setter
ptn1.age = 26

print(ptn1.age)

# Use callback
doctor.view_doctor(ptn1, treatment)