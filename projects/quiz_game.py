questions = (
    "1. What is the capital of Australia?",
    "2. Which planet is known as the Red Planet?",
    "3. Who is known as the Father of the Indian Constitution?",
    "4. Which gas do plants absorb from the atmosphere?",
    "5. Which is the largest ocean in the world?"
)

options = (
    ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Mahatma Gandhi", "B. B. R. Ambedkar", "C. Jawaharlal Nehru", "D. Sardar Patel"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean")
)

answers = ("C", "B", "B", "C", "D")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct! ✅")
    else:
        print("Wrong! ❌")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1

# -------- Results --------

print("\n========== RESULTS ==========")

print("Correct Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Answers:    ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

percentage = (score / len(questions)) * 100

print(f"\nYour Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("Excellent! 🏆")
elif percentage >= 80:
    print("Great Job! 🎉")
elif percentage >= 60:
    print("Good! Keep Practicing 👍")
else:
    print("Keep Learning! 💪")