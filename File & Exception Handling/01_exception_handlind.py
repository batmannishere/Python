try:
     value=float(input("Enter a number: "))
     value=1/value
     print(value)
except ZeroDivisionError:
    print("You cannot divide by zero IDIOT!!")
except ValueError:
    print("Enter a valid number")
finally:
    print("Do some cleanup here")