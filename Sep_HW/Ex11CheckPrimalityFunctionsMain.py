# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no 
# divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.
from Ex11CheckPrimalityFunctions import is_prime

input_number = int(input("Plese enter the number to determine is it prime or not: "))

print(is_prime(input_number))