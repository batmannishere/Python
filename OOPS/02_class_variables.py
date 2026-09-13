class Student:
    qualification="12 pass"
    num_0f_students=0


    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_0f_students+=1  # every time a object is create it will do +1
        
    
student1=Student("Pulkit",19)
student2=Student("batman",25)
print(f"{student2.name} has a done qualification till {student2.qualification} and he is {student2.age} years old")
print(f"{ Student.num_0f_students} students are qualified")