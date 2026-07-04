print("\n------ YOUR SHOPPING CART ------")

for food in foods:
    print(food)

for price in prices:
    total += price

print("-------------------------------")
print(f"Total Bill = ${total:.2f}")

