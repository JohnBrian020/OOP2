class Patient:
    def __init__(self, name, patno, ward):
        self.name = name
        self.patno = patno
        self.ward = ward
      
    def view_patient(self):
        print(
            f"{self.name}, patient no:{self.patno}, "
            f"is at ward {self.ward}"
        )
        
    @property
    def patient_info(self):
        return f"{self.name} - {self.patno} - Ward {self.ward}"
    
patient = Patient("Kamau","P101","Menengai")
print(patient.view_patient())
print(patient.patient_info)