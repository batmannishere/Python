class Student:
    college = "BPIT"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college


print(Student.college)              # BPIT

Student.change_college("IIT")       # how to change first the class.function that needs to be accesed the the value 

print(Student.college)              # hwo to print class.name of the variable in class
