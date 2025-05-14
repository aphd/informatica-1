import random

# Function to generate a random multiplication question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    return num1, num2, correct_answer

# Function to ask the question and check the answer
def ask_question():
    num1, num2, correct_answer = generate_question()
    print(f"What is {num1} x {num2}?")
    try:
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            return True
        else:
            print(f"❌ Wrong. The correct answer is {correct_answer}.\n")
            return False
    except ValueError:
        print("⚠️ Please enter a number.\n")
        return False

# Function to show the menu
def show_menu():
    print("=== Multiplication Practice ===")
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
            if ask_question():
                score += 1
        elif choice == "2":
            print(f"You answered {score} question(s) correctly. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.\n")

# Run the program
if __name__ == "__main__":
    main()
