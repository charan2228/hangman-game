import random

# Word list
words = ["python", "hangman", "developer", "keyboard", "computer", "programming"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6
guessed_letters = []

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    print("Guessed letters:", guessed_letters)
    print(f"Attempts left: {attempts}")
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Good guess!")
        guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
    else:
        print(" Incorrect guess.")
        attempts -= 1

if "_" not in guessed:
    print(f"\n You won! The word was: {word}")
else:
    print(f"\n Game over! The word was: {word}")
