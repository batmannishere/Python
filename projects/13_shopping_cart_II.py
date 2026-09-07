foods = []
prices = []
total = 0

print("===== FOOD ORDER =====")

food = input("Enter a food to buy (q to quit): ")

while not food == "q":

    foods.append(food)

    price = float(input(f"Enter the price of {food}: ₹"))
    prices.append(price)

    total += price

    food = input("Enter a food to buy (q to quit): ")


print("\n===== YOUR ORDER =====")

for i in range(len(foods)):
    print(f"{foods[i]} - ₹{prices[i]:.2f}")

print("----------------------")
print(f"Total: ₹{total:.2f}")

