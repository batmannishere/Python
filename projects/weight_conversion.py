print("===== Weight Converter =====")

weight = float(input("Enter weight: "))
unit = input("Is it in (K)g or (L)b? ").upper()

if unit == "K":
    pounds = weight * 2.20462
    print("Weight in pounds =", pounds)

elif unit == "L":
    kg = weight / 2.20462
    print("Weight in kilograms =", kg)

else:
    print("Invalid input!")