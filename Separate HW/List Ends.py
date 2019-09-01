"""
Exercise 12 (and Solution)

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. For practice, write this code inside a function.
Concepts to practice

    Lists and properties of lists
    List comprehensions (maybe)
    Functions
"""
input_list = [5,10,15,20,25]


def list_ends (input_list):
    l = len(input_list)
    n_list = []
    n_list.append(input_list[0])
    n_list.append(input_list[l])
    print (n_list)