#Amy Cardona
#CIS 129 lab 12
#05-12-2025

# CIS129_Amy_Lab12.py

class Pet:
    def __init__(self, name="", pet_type="", age=0):
        # Set up pet info
        self.__name = name
        self.__type = pet_type
        self.__age = age

    # Set methods
    def setName(self, name):
        self.__name = name

    def setType(self, pet_type):
        self.__type = pet_type

    def setAge(self, age):
        self.__age = age

    # Get methods
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

def main():
    # Create pet
    animal = Pet()

    # Get and validate name (letters only)
    while True:
        name = input("Enter a pet name: ").strip()
        if name.isalpha():
            animal.setName(name)
            break
        else:
            print("Name must contain letters only (no numbers or symbols).")

    # Get type
    pet_type = input("Enter a pet type: ").strip()
    animal.setType(pet_type)

    # Get and validate age (whole number)
    while True:
        age_input = input("Enter a pet age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Please enter a valid whole number for age.")

    animal.setAge(age)

    # Show pet info
    print("\nThe pet name is:", animal.getName())
    print("The pet type is:", animal.getType())
    print("The pet age is:", animal.getAge())

# Run it
if __name__ == "__main__":
    main()

