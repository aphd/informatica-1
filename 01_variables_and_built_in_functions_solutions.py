#################################
# Ex 1
# This program calculates the area and perimeter of a rectangle and then determines which is larger, 
# demonstrating the use of variables and built-in functions in a straightforward manner.

# Assigning values to variables
length = 5
width = 3

# Calculating area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Finding the maximum value between area and perimeter
max_value = max(area, perimeter)

# Displaying the results
print("Area:", area)
print("Perimeter:", perimeter)
print("Maximum value:", max_value)


#################################
# Ex 2
# This program checks whether a number is even or odd using modulo.
number = 7
is_even = number % 2 == 0
result = "even" * is_even + "odd" * (not is_even)
print("The number", number, "is", result)


#################################
# Ex 2 TEST
# This program determines if a number is positive, negative, or zero without using if statements.

number = -3
is_positive = number > 0
is_negative = number < 0
result = ("positive" * is_positive) + ("negative" * is_negative) + ("zero" * (not is_positive and not is_negative))
print(f"The number {number} is {result}.")



##############################
# EX 3
# Write a program that determines if a number is a multiple of 3 or 5 using logical operators.
number = 15
is_multiple_of_3 = number % 3 == 0
is_multiple_of_5 = number % 5 == 0
result = "multiple of 3" * is_multiple_of_3 + "multiple of 5" * is_multiple_of_5
print("The number", number, "is", result or "neither")
