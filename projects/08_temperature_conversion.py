print("===== Temperature Converter =====")

temperature = float(input("Enter temperature: "))
unit = input("Is it in (C)elsius or (F)ahrenheit? ").upper()

if unit == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif unit == "F":
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid input!")