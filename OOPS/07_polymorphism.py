import math
from abc import ABC, abstractmethod
 
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base

    def area(self):
        return self.height*self.base*0.5

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius) # this means super() is the class which we go to have access 
        self.topping=topping   #   the cosntructor the parameter that needs to passed are the paramter necessary that parent class have


shapes=[Circle(4),Square(4),Triangle(3,2),Pizza('Panner',4)]

for shape in shapes:
   print(shape.area())