# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are 
# less than 5.

# Extras:

#     Instead of printing the elements one by one, make a new list that has all
#  the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python.
#     Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.


def ListLessThanTen(inlist,innumber):
    """The function takes a list and a number and returns a new list only with
    number smaller than the specified number
    """
    
    n_list = []
    for i in inlist:
        if i < innumber:
            n_list.append(i)
        elif i >= innumber:
            break
        else:
            raise ValueError
    return (n_list)

if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Pass1" if ListLessThanTen(a,0)==[] else "Error1")
    print("Pass2" if ListLessThanTen(a,14)==[1, 1, 2, 3, 5, 8, 13] else "Error2")
