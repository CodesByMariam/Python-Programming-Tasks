import random

# 5 words ki list
words = ["python", "code", "apple", "mouse", "book", "girl", "mobile"]
word = random.choice(words)

guessed = ["_"] * len(word) # _ _ _ _ bana de ga
lives = 6
guessed_letters = []

print("🎮 Hangman Game Shuru!")
print(f"Word mein {len(word)} letters hain")
print(" ".join(guessed))
print(f"Tumhare paas {lives} chances hain\n")

while lives > 0 and "_" in guessed:
    guess = input("Letter btao: ").lower()

    # Agar pehle likh chuki ho wo letter
    if guess in guessed_letters:
        print("Ye letter to pehle try kar chuki ho! 😄")
        continue

    guessed_letters.append(guess)

    # Agar letter sahi hai
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Wah! Sahi pakra! 👏")
    else:
        lives -= 1
        print(f"Galat! {lives} chances baqi rahe 😔")

    print(" ".join(guessed))
    print("Used letters:", ", ".join(guessed_letters), "\n")

# Game khatam
if "_" not in guessed:
    print(f"🎉 Jeet gayi! Word tha: {word}")
else:
    print(f"💀 Haar gayi! Word tha: {word}")