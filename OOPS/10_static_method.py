class Student:
    @staticmethod
    def is_adult(a):
        if a>=18 :
         return True
        else:
         return False

value= int(input("Enter a age:"))
print(Student.is_adult(value))