class Animal:
    def sleep(self):
        print(f"{self.name} is sleeping")


class Herbivorous(Animal):
    def eat(self):
        print(f"{self.name} eats only grass or vegan food")

    def describe(self):
        print(f"{self.name} is a {self.colour} dog that only eats vegan food")


class Omnivorous(Animal):
    def eat(self):
        print(f"{self.name} eats both veg and non-veg food")

    def describe(self):
        print(f"{self.name} is a {self.colour} animal that eats both veg and non-veg food")


class Pet:
    def play(self):
        print(f"{self.name} likes to play with a ball")


class Dog(Herbivorous, Pet):
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age


class Crow(Omnivorous, Pet):
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age


dog1 = Dog("Bruno", "brown", 2)
crow1 = Crow("Silent", "black", 1)

dog1.eat()
dog1.describe()
dog1.sleep()
dog1.play()

print()

crow1.eat()
crow1.describe()
crow1.sleep()
crow1.play()



