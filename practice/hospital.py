class Patient:
    def __init__(self, name, patno, ward):
        self.name = name #instance properties
        self.patno = patno
        self.ward = ward
    def view_patient(self):
        print(f"{self.name}, patient no: {self.patno}, is at ward{self.ward}")
        
class Doctor:
    def __init__(self, name):
        self.name = name
    def view_doctor(self, patient, callback):
        print(f"{patient.name} is assigned to {self.name}")
        callback(patient, self)
        
def treatment(patient, doctor):
    print(f"{patient.name} has been attended to by {doctor.name}.")

ptn1 = Patient("Kamau","P101","Menengai")
doctor = Doctor("Mr Glen")

#Calling the callback function
doctor.view_doctor(ptn1, treatment)

        