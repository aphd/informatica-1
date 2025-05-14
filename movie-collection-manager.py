# Movie Collection Manager

# List to store movie data
movie_collection = []

# Function to add a new movie
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the director's name: ")
    year = input("Enter the release year: ")
    movie = {"title": title, "director": director, "year": year}
    movie_collection.append(movie)
    print("Movie added successfully!\n")

# Function to search movies by director
def search_by_director():
    name = input("Enter the director's name to search: ")
    found = False
    for movie in movie_collection:
        if movie["director"].lower() == name.lower():
            print(f"{movie['title']} ({movie['year']}) by {movie['director']}")
            found = True
    if not found:
        print("No movies found for this director.\n")

# Function to display all movies sorted by year
def display_movies():
    if not movie_collection:
        print("No movies in the collection.\n")
        return
    print("Movies in your collection (sorted by year):")
    sorted_movies = sorted(movie_collection, key=lambda m: m["year"])
    for movie in sorted_movies:
        print(f"{movie['title']} ({movie['year']}) - {movie['director']}")
    print()

# Function to save movies to a file
def save_to_file():
    filename = input("Enter the filename to save (e.g., movies.txt): ")
    with open(filename, "w") as f:
        for movie in movie_collection:
            line = f"{movie['title']} ({movie['year']}) - {movie['director']}\n"
            f.write(line)
    print("Movie list saved successfully!\n")

# Function to display the menu
def show_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a new movie")
    print("2. Search movies by director")
    print("3. Display all movies")
    print("4. Save movies to a file")
    print("5. Exit")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        print()
        if choice == "1":
            add_movie()
        elif choice == "2":
            search_by_director()
        elif choice == "3":
            display_movies()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.\n")

# Start the program
if __name__ == "__main__":
    main()
