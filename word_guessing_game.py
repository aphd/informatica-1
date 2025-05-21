# # Guess the Hidden Word! Here’s How It Works:

# - The word has **n** letters.
# - You have **n - 3** lives to guess the word.
# - After each incorrect guess, you lose a life, but correct guesses reveal one letter.
# - Try to identify the word before you run out of lives!

# ## Example
# - **Hidden Word**: APPLE
# - **Number of Letters (n)**: 5
# - **Lives Allowed**: 2 (5 - 3)

# ## Gameplay
# - Start with all letters hidden.
# - Make your first guess. If you guess incorrectly, you lose a life. If you guess correctly, one letter will be revealed.
# - Keep guessing until you either find the word or lose all your lives.

# ## Ready? Let’s Begin!
# - **Hidden Word**: _ _ _ _ _ (5 letters)
# - **Lives Left**: 2

### Your guess: ? (Type a letter)

import random

def choose_word():
    # List of words to choose from
    words = ["apple", "banana", "cherry", "grape", "orange"]
    return random.choice(words)

def initialize_game(hidden_word):
    return ["_"] * len(hidden_word), len(hidden_word) - 3

def display_status(guessed_letters, lives):
    print(f"Current Guess: {' '.join(guessed_letters)}")
    print(f"Lives Left: {lives}\n")

def update_guessed_letters(hidden_word, guessed_letters, guess):
    for index, letter in enumerate(hidden_word):
        if letter == guess:
            guessed_letters[index] = guess

def show_menu():
    print("# Guess the Hidden Word! Here’s How It Works:")
    print("- The word has **n** letters.")
    print("- You have **n - 3** lives to guess the word.")
    print("- After each incorrect guess, you lose a life, but correct guesses reveal one letter.")
    print("- Try to identify the word before you run out of lives!\n")

def main():
    show_menu()
    hidden_word = choose_word()
    guessed_letters, lives = initialize_game(hidden_word)
    display_status(guessed_letters, lives)

    while lives > 0:
        guess = input("Your guess (type a letter): ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in hidden_word:
            update_guessed_letters(hidden_word, guessed_letters, guess)
            print("Good guess!")
        else:
            lives -= 1
            print("Wrong guess!")

        display_status(guessed_letters, lives)
        if "_" not in guessed_letters:
            print("Congratulations! You've guessed the word:", hidden_word)
            return

    print("Sorry, you've run out of lives. The word was:", hidden_word)

# Start the game
main()