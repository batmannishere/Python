item=input("Enter food u would like to have: ")
price=float(input(f"price of {item} is:"))
quantity=int(input(f"how many {item} would u like to have"))
total=price*quantity
print(f"Your amount to be paid is ${total}")