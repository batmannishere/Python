class Student:
    def __init__(self,name,age):
     self.name=name
     self.age=age

    def introduce(self):#
        print(f"My name is {self.name} and I am {self.age} yrs old")

s1=Student("Pulkit",20)
s1.introduce()
