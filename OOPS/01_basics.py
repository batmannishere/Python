from car import Car

car1=Car("mustang",2024,"yellow","not for sale") # to make an object name it then add name of the class(then we will pass the parameters)
print(car1.model) # to access we will write name of the object . what we need to access like model,year or for sale
print(car1.year)
print(car1.colour)
print(car1.for_sale)
car1.drive()