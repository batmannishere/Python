class Animal:
    alive= True

class Dog(Animal):
    def speak(self):
        print(f"whoof")

class Cat(Animal):
    def speak(self):
        print(f"whoof")


class Car:
    def speak(self):
        print("Rwarr")



animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()