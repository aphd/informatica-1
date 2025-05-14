def generate_random_multiplication():
    pass

def ask_questions():
    num1, num2, correct_answer = 3, 5, 15
    print(f"what is {num1} x {num2}?")
    user_answer = int(input("Your answer: "))
    if user_answer == correct_answer:
        print("✅  correct")
    else:
        print(f"❌ Wrong. the correct answer is {correct_answer}")

def show_menu():
    print("\n\033[1m===== multiplication quiz =====\033[0m")
    print("1 new question")
    print("2 exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            ask_questions()
        elif choice == "2":
            break
        else:
            print("\033[31mInvalid option\033[0m")

main()