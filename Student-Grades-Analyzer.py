# Function to collect student data from user
def get_student():
    student_scores = {}
    num_students = int(input("How many students? "))

    for _ in range(num_students):
        name = input("Enter student name: ")
        scores = input(f"Enter math scores for {name} (comma-separated): ")
        score_list = [int(score.strip()) for score in scores.split(",") if score.strip().isdigit()]
        student_scores[name] = score_list

    return student_scores

# Function to compute average score for each student
def get_average(scores_dict):
    averages = {}
    for student, scores in scores_dict.items():
        avg = sum(scores) / len(scores)
        averages[student] = avg
    return averages

# Function to find top student(s)
def get_top_student(averages_dict):
    max_avg = max(averages_dict.values())
    top_students = [student for student, avg in averages_dict.items() if avg == max_avg]
    return top_students, max_avg

# Function to print all students and their average
def print_result(averages_dict, top_students, top_score):
    print("\nStudent Averages:")
    for student, avg in averages_dict.items():
        print(f"{student}: {avg:.2f}")

    print(f"\nTop student(s) with average score {top_score:.2f}:")
    for student in top_students:
        print(f"🏅 {student}")

# Main function
def main():
    print("=== Student Grades Analyzer ===")
    student_scores = get_student()

    if not student_scores:
        print("No data entered.")
        return

    averages = get_average(student_scores)
    top_students, top_score = get_top_student(averages)
    print_result(averages, top_students, top_score)

# Run the program
if __name__ == "__main__":
    main()