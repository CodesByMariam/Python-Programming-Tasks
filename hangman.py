import random

# List of 5-letter words
words = ["python", "code", "apple", "mouse", "book", "girl", "mobile"]
word = random.choice(words)

guessed = ["_"] * len(word) # it will make _ _
lives = 6
guessed_letters = []

print("🎮 Hangman Game Started!")
print(f"The word has {len(word)} letters")
print(" ".join(guessed))
print(f"You have {lives} chances\n")

while lives > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    # If you already tried this letter
    if guess in guessed_letters:
        print("You already tried this letter! 😄")
        continue

    guessed_letters.append(guess)

    # If the letter is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Great! Correct guess! 👏")
    else:
        lives -= 1
        print(f"Wrong! You have {lives} chances left 😔")

    print(" ".join(guessed))
    print("Used letters:", ", ".join(guessed_letters), "\n")

# Game over
if "_" not in guessed:
    print(f"🎉 You Won! The word was: {word}")
else:
    print(f"💀 You Lost! The word was: {word}")
