class Animal:
    def __init__(self,name,colour,age):
        self.name=name
        self.colour=colour
        self.age=age


    def eat(self):
        print(f"{self.name} is eating right now")
    def sleep(self):
        print(f"{self.name} is sleeping ")
    def walk(self):
        print(f"{self.name} need a walk")




class cat(Animal):
   def speak(self ):
    print("MEOW!!")


class dog(Animal):
   def speak(self):
    print("WHOOF!!")



dog1=dog("bruno","brown",2)
cat1=cat("mickey","orange",5)


dog1.speak()
