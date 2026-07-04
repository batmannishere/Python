menu = {
    "popcorn": 5.00,
    "soft drink": 3.50,
    "hot dog": 4.50,
    "burger": 7.00,
    "french fries": 4.00,
    "pizza slice": 6.00,
    "taco": 5.50,
    "pretzel": 3.00,
    "corn dog": 4.00,
    "nachos": 5.50,
    "chicken nuggets": 6.50,
    "ice cream": 4.00,
    "cookie": 2.50,
    "chocolate bar": 2.00,
    "candy": 1.50,
    "cupcake": 3.50,
    "coffee": 3.00,
    "juice": 3.50,
    "bottled water": 2.00,
    "donut": 2.50
}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:20}: ${value:.2f}")

print("------------------------")

while True:
    item = input("Enter an item to buy (q to quit): ").lower()

    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
    else:
        print("Item not available!")

print("\n------ YOUR CART ------")

for food in cart:
    print(food)
    total += menu.get(food)

print("-----------------------")
print(f"Total: ${total:.2f}")