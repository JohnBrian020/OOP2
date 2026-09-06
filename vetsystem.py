# Clinic syste,
# Name that must be a string btwn 1 and 25 Characters
# Breed that must be selected from an approved list

# Approved list
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

def __init__(self, name='Fido', breed='Mastiff'):
    self.name = name # Uses the setter to validate input
    self.breed = breed # # Uses the setter to validate input
    
    @property
    def name(self):
        """The name property"""
        return self._name
    
    @name.setter
    def name(self,name):
        """Ensure name is a string between 1 and 25 characters."""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")
        
    @breed.setter
    def breed(self, name):
        """Ensure breed is in the list of approved breeds."""
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in the list of approved breeds.")