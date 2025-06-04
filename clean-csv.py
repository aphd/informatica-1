import csv

def remove_commas_in_names(input_file="olympic_medals.csv", output_file="olympic_medals_cleaned.csv"):
    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Remove commas from the Name field only
            row['Name'] = row['Name'].replace(',', '')
            writer.writerow(row)

if __name__ == "__main__":
    remove_commas_in_names()
