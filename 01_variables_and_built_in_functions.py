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
# TODO

##############################
# EX 3
# Write a program that determines if a number is a multiple of 3 or 5 using logical operators.
number = 15
# TODO


###############################
# Ex 3
# This program generates a list of squares of numbers from 1 to 5 using the map function.

# ​In Python, a lambda function is a concise way to define an anonymous function—that is, a function without a name.
squares = list(map(lambda x: x**2, range(1, 6)))
print("Squares from 1 to 5:", squares)

