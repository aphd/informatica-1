def read_file(filepath):
    # with open(filepath, 'r', encoding='utf-8') as file: 
    #     lines = file.readlines()
    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

def get_categories(data):
    categories = set(row[1] for row in data)
    return sorted(categories)

def count_by_city(data):
    city_counts = {}
    for row in data:
        city = row[4]
        city_counts[city] = city_counts.get(city, 0) + 1

    def get_count(item):
        return item[1]

    return max(city_counts.items(), key=get_count) # return max(city_counts.items(), key=lambda x:x[1]) 
    

def count_by_country_and_category(data):
    """Return a dictionary with categories as keys and the country with the most prizes in that category."""
    category_country = {}
    for row in data:
        category = row[1]
        country = row[5]
        if category not in category_country:
            category_country[category] = {}
        category_country[category][country] = category_country[category].get(country, 0) + 1
    
    result = {}
    for category, countries in category_country.items():
        max_country = max(countries.items(), key=lambda x: x[1])
        result[category] = max_country
    return result

def display_menu():
    """Display the main menu."""
    print("\n--- Nobel Prize Data Menu ---")
    print("1. Show all Nobel Prize categories")
    print("2. Find the city with the most Nobel Prize winners")
    print("3. Find the country with most Nobel Prizes by category")
    print("4. Exit")

def main():
    filepath = 'nobel-prize.csv'
    header, data = read_file(filepath)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            categories = get_categories(data)
            print("Categories:")
            for cat in categories:
                print("-", cat)
        elif choice == '2':
            city, count = count_by_city(data)
            print(f"The city with the most Nobel Prize winners is {city} with {count} winners.")
        elif choice == '3':
            result = count_by_country_and_category(data)
            for category, (country, count) in result.items():
                print(f"{category.capitalize()}: {country} ({count})")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
