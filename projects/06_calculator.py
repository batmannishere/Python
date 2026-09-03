num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("enter operation: ")
if operator== "+":
   print(round(num1+num2,2))
elif operator== "-":
    print(round(num1-num2,2))
elif operator== "/":
    print(round(num1/num2,2))
elif operator=="%":
    print(round(num1%num2,2))
elif operator=="*":
    print(round(num1*num2,2))
else:
    print(f"{operator} is not a valid operator")