principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount can't be zero or negative.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate (%): "))
    if rate <= 0:
        print("Interest rate can't be zero or negative.")

while time <= 0:
    time = float(input("Enter the time (in years): "))
    if time <= 0:
        print("Time can't be zero or negative.")

amount = principal * pow((1 + rate / 100), time)

print("Amount =", round(amount, 2))