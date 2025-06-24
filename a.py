import random

# Step 1: Define a small list of words
words = ["apple", "banana", "grape", "orange", "cherry"]

# Step 2: Randomly select a word from the list
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

# Step 3: Game loop
print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))

while attempts_left > 0:
    # Step 4: Show current guessed progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())

    # Step 5: Ask for a letter guess
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guess to guessed list
    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print("❌ Wrong guess. Attempts left:", attempts_left)

    # Win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    # If attempts run out
    print("\n💀 Game Over! The word was:", secret_word)
