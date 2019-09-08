"""
Exercise 12 (and Solution)

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. For practice, write this code inside a function.
Concepts to practice

    Lists and properties of lists
    List comprehensions (maybe)
    Functions
"""



def list_ends(in_list):
    l = len(in_list)-1
    n_list = []
    n_list.append(in_list[0])
    n_list.append(in_list[l])
    return (n_list)

