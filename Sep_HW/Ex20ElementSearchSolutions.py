"""
 Element Search
Exercise 20 (and Solution)

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
to largest) and another number. The function decides whether or not the given number is inside the list 
and returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
"""
def ElementSearch(inlist, innumber):
    if innumber in inlist:
        return True
    else:
        return False

if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print("Pass1" if ElementSearch(l, 5) == False else "Error1") # prints False
  print("Pass2" if ElementSearch(l, 10) == True else "Error2") # prints True
  print("Pass3" if ElementSearch(l, -1) == False else "Error3") # prints False
  print("Pass4" if ElementSearch(l, 2) == True else "Error4") # prints True
