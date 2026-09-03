print("===== COMPOUND INTEREST CALCULATOR =====")

principal = float(input("Enter principal amount: "))

while principal <= 0:
    print("Invalid input! Principal must be greater than 0.")
    principal = float(input("Enter principal amount: "))


rate = float(input("Enter rate of interest (%): "))

while rate < 0:
    print("Invalid input! Rate cannot be negative.")
    rate = float(input("Enter rate of interest (%): "))


time = float(input("Enter time (in years): "))

while time < 0:
    print("Invalid input! Time cannot be negative.")
    time = float(input("Enter time (in years): "))


final_amount = principal * pow((1 + (rate / 100)), time)
compound_interest = final_amount - principal


print("\n===== RESULT =====")
print(f"Principal:          ₹{principal:.2f}")
print(f"Rate:               {rate:.2f}%")
print(f"Time:               {time:.2f} years")
print(f"Compound Interest:  ₹{compound_interest:.2f}")
print(f"Final Amount:       ₹{final_amount:.2f}")
