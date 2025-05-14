# Function to compute average score for each student
def compute_averages(scores_dict):
    averages = {}
    for student, scores in scores_dict.items():
        avg = sum(scores) / len(scores)
        averages[student] = avg
    return averages

# Function to print all students and their average
def print_averages(averages_dict):
    print("\nStudent Averages:")
    for student, avg in averages_dict.items():
        print(f"{student}: {avg:.2f}")
    print()

# Function to find top student(s)
def find_top_students(averages_dict):
    max_avg = max(averages_dict.values())
    top_students = [student for student, avg in averages_dict.items() if avg == max_avg]
    return top_students, max_avg

# Function to collect student data from user
def get_student_scores():
    student_scores = {}
    num_students = int(input("How many students? "))

    for _ in range(num_students):
        name = input("Enter student name: ")
        scores = input(f"Enter math scores for {name} (comma-separated): ")
        score_list = [int(score.strip()) for score in scores.split(",") if score.strip().isdigit()]
        student_scores[name] = score_list

    return student_scores

# Main function
def main():
    print("=== Student Grades Analyzer ===")
    student_scores = get_student_scores()

    if not student_scores:
        print("No data entered.")
        return

    averages = compute_averages(student_scores)
    print_averages(averages)

    top_students, top_score = find_top_students(averages)
    print(f"Top student(s) with average score {top_score:.2f}:")
    for student in top_students:
        print(f"🏅 {student}")

# Run the program
if __name__ == "__main__":
    main()
     