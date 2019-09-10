from Ex13Fibonacci import *

howMany = input("How many numbers do you want me to generate? ")

if int(howMany) >= 0:
    print(FibonnaciGenerator(howMany))
else: 
    print("Numbers quantity can't be negative")
    quit()

"""
ToDo
1. 0-3 input options realization
2. Input checking in main or in lib
3. Auto tests.
"""