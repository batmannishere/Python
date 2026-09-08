import random

low_number = int(input("Enter the starting range: "))
high_number = int(input("Enter the ending range: "))

answer = random.randint(low_number, high_number)

guesses = 0

print("\nPython Number Guessing Game:")
print(f"Select a number between {low_number} and {high_number}")

guessing = True

while guessing:

    guess = input("Enter your guess: ")

    if guess.isalpha():
        print("Please enter a valid number!")

    else:
        guess = int(guess)
        guesses += 1

        if guess < answer:
            print("Too low!")

        elif guess > answer:
            print("Too high!")

        else:
            print(f"🎉 Correct! The answer was {answer}")
            print(f"You guessed it in {guesses} attempts!")
            guessing = False