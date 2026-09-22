def add_sprinkler(func):

    def wrapper(): #if this is not added it will print the function ice_cream without even calling it 
        print("added blue sprinkler on icecream")
        func()

    return wrapper


@add_sprinkler
def ice_cream():
    print("Chocolate ice cream is my favourite")


ice_cream()