def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           -
        """,
        """
           ------
           |    |
           |    O
           |
           |
           -
        """,
        """
           ------
           |    |
           |
           |
           |
           -
        """,
        """
           ------
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print("Guessed letters:", " ".join(guessed_letters))

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(word_display))

        guess = input("Guess a letter: ").lower()

        if guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Letter is not in word.")

    if tries == 0:
        print(display_hangman(tries))
        print(f"You lost! The word was {word}")
    else:
        print(f"You guessed the word {word}!")

play_again = "y"
while play_again == "y":
    play()
    play_again = input("Play again? (y/n): ").lower()