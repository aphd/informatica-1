import random

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random number and ask the user
def ask_prime_question():
    number = random.randint(1, 100)
    print(f"Is {number} a prime number? (yes/no)")
    answer = input("Your answer: ").strip().lower()

    correct = is_prime(number)

    if (answer == "yes" and correct) or (answer == "no" and not correct):
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Incorrect. The correct answer is {'yes' if correct else 'no'}.\n")
        return False

# Show the main menu
def show_menu():
    print("=== Prime Number Quiz ===")
    print("1. New Question")
    print("2. Exit")

# Main function
def main():
    score = 0
    while True:
        show_menu()
        choice = input("Choose an option (1-2): ")
        print()
        if choice == "1":
            if ask_prime_question():
                score += 1
        elif choice == "2":
            print(f"You got {score} question(s) right. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

# Run the program
if __name__ == "__main__":
    main()
