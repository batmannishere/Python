import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

print(roll())

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print(roll())
    roll_again = input("Roll again? ").lower()