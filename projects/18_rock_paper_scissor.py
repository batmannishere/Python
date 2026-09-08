import random

options = ["rock", "paper", "scissors"]

while True:
    player = input("Enter a choice (rock, paper, scissors) or 'q' to quit: ").lower()

    if player == "q":
        print("Thanks for playing!")
        break

    if player not in options:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(options)
    print(f"Player chose {player}, Computer chose {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    print()