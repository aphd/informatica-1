# 🧪 Exercise: Nobel Prize Data Analysis

## 📝 Description
Write a Python program to analyze Nobel Prize data from a CSV file.  
The file contains information about Nobel Prize winners, including their name, year, category, country, and more.

---

## 🧾 Requirements

- Read and parse a CSV file **manually**, without using any external libraries like `csv` or `pandas`.
- Structure your code using **modular functions** — each function should perform a single, well-defined task.
- Create a **menu-driven interface** that allows the user to choose among the following options:

---

## 📋 Menu Options

1. Show all Nobel Prize categories
2. Find the city with the most Nobel Prize winners
3. Find the country with most Nobel Prizes by category
4. Exit

---

## 📂 Notes

- Use only **built-in Python features** (`open()`, loops, string methods, etc.).
- Assume the input file is named `nobel-prize.csv` and uses the following header:

```
Year,Category,Name,Birthdate,Birth Place,County,Residence,Role/Affiliate,Field/Language,Prize Name,Motivation
```

---
## 📚 Additional Task Ideas

1. 🧓 Find the Oldest/Youngest Nobel Prize Winner
Calculate the age at the time of award using Year and Birthdate.

Find and print the name of the oldest laureate at the time they received the prize.

2. 🧠 Keyword Search in Motivation
Allow the user to input a keyword (e.g., "peace", "physics").

Print all entries where that keyword appears in the Motivation text.

3. 🏆 List Laureates Who Won Multiple Prizes (if any)
Some individuals may appear more than once in the data.

Identify and print their names and categories.

4. 🔍 Advanced: Search by Partial Name
Let the user enter a partial name (e.g., “Einstein” or “Marie”).

Return matching entries, including full name, year, and category.