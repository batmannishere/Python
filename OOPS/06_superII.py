class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"{self.name} is {self.age} years old")


class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    
    
        
    def info(self):
        super().info()
        print("whoof")
        


