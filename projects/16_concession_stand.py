menu = {
    "popcorn": 150,
    "nachos": 120,
    "burger": 100,
    "pizza": 200,
    "coke": 60,
    "water": 30,
    "chips": 50,
    "chocolate": 80
}

cart = []
quantities = []
total = 0


print("========== MENU ==========")

for food, price in menu.items():
    print(f"{food.title():<15} ₹{price:.2f}")

print("==========================")

food = input("\nEnter the food you would like to add (q to quit): ")

while not food == 'q':

    if menu.get(food):

        cart.append(food)

        quantity = int(input(f"How many {food} would you like to have? "))
        quantities.append(quantity)

        food = input("\nEnter the food you would like to add (q to quit): ")

    else:

        print("This item is not in our menu!")
        food = input("Enter the food you would like to add: ")


print("\n========== YOUR CART ==========")

for item in range(len(cart)):

    price = menu[cart[item]]
    item_total = price * quantities[item]
    total += item_total

    print(f"{cart[item].title():<15} x {quantities[item]:<3} ₹{item_total:.2f}")

print("--------------------------------")
print(f"{'TOTAL:':<20} ₹{total:,.2f}")
print("================================")
print("      Thank you for ordering! 😊")
        