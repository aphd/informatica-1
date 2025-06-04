def load_data(filename="olympic_analysis.csv"):
    data = []
    file = open(filename, encoding='utf-8')
    lines = file.readlines()
    headers = lines[0].strip().split(",")
    for line in lines[1:]:
        cols = line.strip().split(",")
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = cols[i]
        row['Age'] = int(row['Age'])
        row['Gold Medal'] = int(row['Gold Medal'])
        row['Silver Medal'] = int(row['Silver Medal'])
        row['Bronze Medal'] = int(row['Bronze Medal'])
        data.append(row)
    return data

def total_medals(data, country):
    total = 0
    for row in data:
        if row['Country'].lower() == country.lower():
            total += row['Gold Medal'] + row['Silver Medal'] + row['Bronze Medal']
    return total

def average_age(data, country):
    ages = [row['Age'] for row in data if row['Country'].lower() == country.lower()]
    if not ages:
        return None
    return round(sum(ages) / len(ages), 2)

def top_athlete(data, country):
    athlete_medals = {}
    for row in data:
        if row['Country'].lower() == country.lower():
            name = row['Name']
            medals = row['Gold Medal'] + row['Silver Medal'] + row['Bronze Medal']
            athlete_medals[name] = athlete_medals.get(name, 0) + medals
    if not athlete_medals:
        return None, 0
    top_name = max(athlete_medals, key=athlete_medals.get)
    return top_name, athlete_medals[top_name]

def top_gold_country(data):
    country_gold = {}
    for row in data:
        country = row['Country']
        country_gold[country] = country_gold.get(country, 0) + row['Gold Medal']
    if not country_gold:
        return None, 0
    top_country = max(country_gold, key=country_gold.get)
    return top_country, country_gold[top_country]

def list_sports(data):
    sports = set()
    for row in data:
        sports.add(row['Sport'])
    return sorted(sports)

def top_athlete_in_sport(data, sport):
    athlete_medals = {}
    for row in data:
        if row['Sport'].lower() == sport.lower():
            name = row['Name']
            medals = row['Gold Medal'] + row['Silver Medal'] + row['Bronze Medal']
            athlete_medals[name] = athlete_medals.get(name, 0) + medals
    if not athlete_medals:
        return None, 0
    top_name = max(athlete_medals, key=athlete_medals.get)
    return top_name, athlete_medals[top_name]

def top_gold_athlete_in_sport(data, sport):
    athlete_gold = {}
    for row in data:
        if row['Sport'].lower() == sport.lower():
            name = row['Name']
            gold = row['Gold Medal']
            athlete_gold[name] = athlete_gold.get(name, 0) + gold
    if not athlete_gold:
        return None, 0
    top_name = max(athlete_gold, key=athlete_gold.get)
    return top_name, athlete_gold[top_name]

def show_menu():
    print("\n===== Olympic Medals Analysis Menu =====")
    print("1. Get total medals for a country")
    print("2. Get average age of athletes from a country")
    print("3. Get top athlete (most medals) from a country")
    print("4. Find country with most gold medals")
    print("5. List all sports")
    print("6. Top athlete (most medals) in a sport")
    print("7. Athlete with most gold medals in a sport")
    print("8. Exit")

def get_user_choice():
    return input("Enter your choice (1-8): ").strip()

def print_green(text):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(f"{GREEN}{text}{RESET}")

def print_red(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}{text}{RESET}")

def handle_choice(choice, data):
    if choice == "1":
        country = input("Enter country name: ")
        print_green(f"Total medals for {country}: {total_medals(data, country)}")
    elif choice == "2":
        country = input("Enter country name: ")
        avg = average_age(data, country)
        print_green(f"Average age of athletes from {country}: {avg if avg is not None else 'No data'}")
    elif choice == "3":
        country = input("Enter country name: ")
        name, medals = top_athlete(data, country)
        if name:
            print_green(f"Top athlete from {country}: {name} ({medals} medals)")
        else:
            print_red("No data found.")
    elif choice == "4":
        country, golds = top_gold_country(data)
        print_green(f"Country with most gold medals: {country} ({golds} gold medals)")
    elif choice == "5":
        sports = list_sports(data)
        print_green("Sports in dataset:")
        for s in sports:
            print(f"- {s}")
    elif choice == "6":
        sport = input("Enter sport name: ")
        name, medals = top_athlete_in_sport(data, sport)
        if name:
            print_green(f"Top athlete in {sport}: {name} ({medals} medals)")
        else:
            print_red("No data found.")
    elif choice == "7":
        sport = input("Enter sport name: ")
        name, golds = top_gold_athlete_in_sport(data, sport)
        if name:
            print_green(f"Athlete with most gold medals in {sport}: {name} ({golds} gold medals)")
        else:
            print_red("No data found.")
    elif choice == "8":
        print_red("Exiting. Goodbye!")
        return False
    else:
        print("Invalid choice.")
    return True

def main():
    data = load_data()
    if not data:
        print("No data loaded. Exiting.")
        return
    while True:
        show_menu()
        choice = get_user_choice()
        if not handle_choice(choice, data):
            break

if __name__ == "__main__":
    main()
