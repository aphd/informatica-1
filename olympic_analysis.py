def load_data(filename="olympic_medals.csv"):
    data = []
    try:
        with open(filename, encoding='utf-8') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(",")
            for line in lines[1:]:
                parts = line.strip().split(",")
                if len(parts) != len(headers):
                    continue
                row = {}
                for i in range(len(headers)):
                    row[headers[i]] = parts[i]
                try:
                    row['Age'] = int(row['Age'])
                    row['Gold Medal'] = int(row['Gold Medal'])
                    row['Silver Medal'] = int(row['Silver Medal'])
                    row['Bronze Medal'] = int(row['Bronze Medal'])
                    data.append(row)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("CSV file not found.")
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
            if name in athlete_medals:
                athlete_medals[name] += medals
            else:
                athlete_medals[name] = medals
    top_name = None
    max_medals = -1
    for name in athlete_medals:
        if athlete_medals[name] > max_medals:
            max_medals = athlete_medals[name]
            top_name = name
    return (top_name, max_medals) if top_name else (None, 0)

def top_gold_country(data):
    country_gold = {}
    for row in data:
        country = row['Country']
        gold = row['Gold Medal']
        if country in country_gold:
            country_gold[country] += gold
        else:
            country_gold[country] = gold
    top_country = None
    max_gold = -1
    for country in country_gold:
        if country_gold[country] > max_gold:
            max_gold = country_gold[country]
            top_country = country
    return (top_country, max_gold) if top_country else (None, 0)

def show_menu():
    print("\n===== Olympic Medals Analysis Menu =====")
    print("1. Get total medals for a country")
    print("2. Get average age of athletes from a country")
    print("3. Get top athlete (most medals) from a country")
    print("4. Find country with most gold medals")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice (1-5): ").strip()

def handle_choice(choice, data):
    if choice == "1":
        country = input("Enter country name: ")
        print(f"Total medals for {country}: {total_medals(data, country)}")
    elif choice == "2":
        country = input("Enter country name: ")
        avg = average_age(data, country)
        print(f"Average age of athletes from {country}: {avg if avg else 'No data'}")
    elif choice == "3":
        country = input("Enter country name: ")
        name, medals = top_athlete(data, country)
        if name:
            print(f"Top athlete from {country}: {name} ({medals} medals)")
        else:
            print("No data found.")
    elif choice == "4":
        country, golds = top_gold_country(data)
        print(f"Country with most gold medals: {country} ({golds} gold medals)")
    elif choice == "5":
        print("Exiting. Goodbye!")
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
