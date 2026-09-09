balance = 0
is_running = True

while is_running:
    action = input("Would you like to check your (b)alance, (d)eposit, (w)ithdraw, or (q)uit?: ").lower()

    if action == "b":
        print(f"Your balance is ${balance}")
    elif action == "d":
        deposit = float(input("How much would you like to deposit? $"))
        if deposit > 0:
            balance += deposit
        else:
            print("Invalid amount!")
    elif action == "w":
        withdrawal = float(input("How much would you like to withdraw? $"))
        if withdrawal <= balance:
            balance -= withdrawal
        else:
            print("Insufficient funds!")
    elif action == "q":
        is_running = False
    else:
        print("Invalid action!")

print("Thanks for banking with us!")