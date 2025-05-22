# Create a program to manage a collection of books, 
# incorporating advanced math features. 
# The program should allow users to 
# add books, 
# search for books by author, 
# display all books, 
# calculate the average rating, 
# find the highest and lowest ratings, 
# and save the collection to a file.

# Requirements
# Add a New Book: Prompt the user to enter the book title, author, publication year, and rating (out of 10). Store this information in a list of dictionaries.
# Search Books by Author: Allow the user to search for books by entering an author's name. Display all books by that author.
# Display All Books: Show all books in the collection sorted alphabetically by title.
# Calculate Average Rating: Provide an option to calculate and display the average rating of all books in the collection.
# Find Highest and Lowest Ratings: Provide an option to display the highest and lowest ratings among the books.
# Save Books to a File: Save the list of books to a specified text file.
# Menu System: Implement a menu system to allow users to choose options. 

# The menu should include the following:
# Add a new book
# Search books by author
# Display all books
# Calculate average rating
# Find highest and lowest ratings
# Save books to a file
# Exit

# Book Collection Manager with Advanced Math Features

# List to store book data
book_collection = []

# Function to add a new book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")
    rating = float(input("Enter the rating (out of 10): "))
    book = {"title": title, "author": author, "year": year, "rating": rating}
    book_collection.append(book)
    print("Book added successfully!\n")

# Function to search books by author
def search_by_author():
    name = input("Enter the author's name to search: ")
    found = False
    for book in book_collection:
        if book["author"].lower() == name.lower():
            print(f"{book['title']} ({book['year']}) by {book['author']} - Rating: {book['rating']}/10")
            found = True
    if not found:
        print("No books found for this author.\n")

# Function to display all books sorted by title
def display_books():
    if not book_collection:
        print("No books in the collection.\n")
        return
    print("Books in your collection (sorted by title):")
    sorted_books = sorted(book_collection, key=lambda b: b["title"])
    for book in sorted_books:
        print(f"{book['title']} ({book['year']}) - {book['author']} - Rating: {book['rating']}/10")
    print()

# Function to calculate average rating
def calculate_average_rating():
    if not book_collection:
        print("No books in the collection to calculate the average rating.\n")
        return
    total_rating = sum(book["rating"] for book in book_collection)
    average_rating = total_rating / len(book_collection)
    print(f"Average rating of all books: {average_rating:.2f}/10\n")

# Function to find highest and lowest ratings
def find_high_low_ratings():
    if not book_collection:
        print("No books in the collection to find ratings.\n")
        return
    highest_rating = max(book["rating"] for book in book_collection)
    lowest_rating = min(book["rating"] for book in book_collection)
    print(f"Highest rating: {highest_rating}/10")
    print(f"Lowest rating: {lowest_rating}/10\n")

# Function to save books to a file
def save_to_file():
    filename = input("Enter the filename to save (e.g., books.txt): ")
    with open(filename, "w") as f:
        for book in book_collection:
            line = f"{book['title']} ({book['year']}) - {book['author']} - Rating: {book['rating']}\n"
            f.write(line)
    print("Book list saved successfully!\n")

# Function to display the menu
def show_menu():
    print("=== Book Collection Manager ===")
    print("1. Add a new book")
    print("2. Search books by author")
    print("3. Display all books")
    print("4. Calculate average rating")
    print("5. Find highest and lowest ratings")
    print("6. Save books to a file")
    print("7. Exit")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")
        print()
        if choice == "1":
            add_book()
        elif choice == "2":
            search_by_author()
        elif choice == "3":
            display_books()
        elif choice == "4":
            calculate_average_rating()
        elif choice == "5":
            find_high_low_ratings()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 7.\n")

# Start the program
if __name__ == "__main__":
    main()