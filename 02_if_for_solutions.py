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
for i in range(1, 101):
    if i % 2 != 0:
        total_sum += i
print(total_sum)

# EX 11
# Count how many vowels are in a string
text = "Programming is fun"
vowels = "aeiouAEIOU"
count = 0
for c in text:
    if c in vowels:
        count += 1
print(count)

# EX 3
# Check if a number is prime
number = 81
is_prime = True
for i in range(2, int(number**0.5) + 1): # Factor Pairs: if a number n is not prime -> n = a x b
    if number % i == 0:
        is_prime = False
        break

print(f"{number} is prime: {is_prime}")

#EX 4
# Print All Prime Numbers Between 1 and 100
for number in range(2, 100):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

# EX 5
# Print the factorial of a number
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# EX 8
# Reverse a string
s = "hello"
rev = ""
for char in s:
    rev = char + rev
print(rev)

# EX 6
# Count digits in a number (//=)
n = 123456
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)

# EX 9
# Sum of digits of a number
n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

# EX 7
# Print the Fibonacci sequence up to 10 terms
a, b = 0, 1
for _ in range(10):
    print(a) 
    a, b = b, a + b # simultaneous assignment


# Ec 11
# Check Armstrong Number
n = 153
sum_cubes = sum(int(digit) ** 3 for digit in str(n))
print(sum_cubes == n)

# EX 12
# GCD of Two Numbers (MCD)
a, b = 97, 11
while b:
    a, b = b, a % b
print(a)

# EX 10
# Check if a number is a palindrome
n = 121
original = str(n)
reversed_n = original[::-1]
print(original == reversed_n)

# Check if a number is a perfect square:
num = 25
is_square = False
for i in range(1, num + 1):
    if i * i == num:
        is_square = True
        break
print(is_square)


# Check if a number is a power of 2:
num = 16
is_power_of_two = False
if num > 0:
    while num % 2 == 0:
        num //= 2
    if num == 1:
        is_power_of_two = True
print(is_power_of_two)

# Check if a number is an Automorphic Number
num = 6
square = num * num
if square % (10 ** len(str(num))) == num:
    print(True)
else:
    print(False)