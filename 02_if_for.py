# Ex 1
# Write a Python program that calculates the sum of all even numbers from 1 to 100. 
# Use a loop to iterate through the numbers and an if statement to check if each number is even. 
# Finally, print the total sum.
total_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_sum += i
print(total_sum)

# EX 2
# Write a Python program that calculates the sum of all odd numbers from 1 to 100. 
# Use a loop to iterate through the numbers and an if statement to check if each number is odd. 
# Finally, print the total sum.
total_sum = 0
# TODO

# EX 3
# Check if a number is prime (A prime number is only divisible by 1 and itself.)
number = 81
is_prime = True
for i in range(2, int(number**0.5) + 1): # Factor Pairs: if a number n is not prime -> n = a x b
    if number % i == 0:
        is_prime = False
        break

print(f"{number} is prime: {is_prime}")

# EX 4
# Print All Prime Numbers Between 1 and 100
# TODO
