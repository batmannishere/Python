import random

def spin_row():
    symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]
    row = [random.choice(symbols) for _ in range(3)]
    return row

def print_row(row):
    print(" | ".join(row))

def check_row(row):
    return row[0] == row[1] == row[2]

def spin():
    balance = 100
    bet = 0

    while True:
        print(f"Balance: ${balance}")
        bet = int(input("Place a bet: $"))
        if bet > balance:
            print("Insufficient funds!")
            continue
        break

    row = spin_row()
    print_row(row)

    if check_row(row):
        winnings = bet * 3
        print(f"You won ${winnings}!")
        balance += winnings
    else:
        print(f"You lost ${bet}!")
        balance -= bet

    return balance

play_again = "y"
balance = 100

while play_again == "y":
    balance = spin()
    play_again = input("Spin again? (y/n): ").lower()
    if balance <= 0:
        print("You're out of money!")
        break