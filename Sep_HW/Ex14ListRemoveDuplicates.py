# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def ListRemoveDuplicates(user_list):
    '''Takes a list and return a list without duplicates. Loops realization.'''
    unique_list = []
    for i in user_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue
    return unique_list


def ListRemoveDuplicatesSets(user_list):
    '''Takes a list and return a list without duplicates. Sets realization.'''
    pass



def test_RemoveDuplicates(remdupl_algorithm):
    '''Testing any remove dulplicates algorithm by feeding it data and
    checking output. Argument is the name of remove duplicates function
    '''
    print("Testing", remdupl_algorithm.__name__)
    test_remdupl_TC1(remdupl_algorithm)
    test_remdupl_TC2(remdupl_algorithm)



def test_remdupl_TC1(remdupl_algorithm):
    '''Basic TC with [1,...5] array'''
    num = [1, 2, 3, 3, 3, 3, 4, 10, 3, 4, 1, 2, 0]
    num_unique = [1, 2, 3, 4, 10, 0]
    print("TC1", "Passed" if remdupl_algorithm(num) == num_unique else "Failed")

def test_remdupl_TC2(remdupl_algorithm):
    '''TC with empty list'''
    num = []
    num_unique = []
    print("TC2", "Passed" if remdupl_algorithm(num) == num_unique else "Failed")


if __name__ == "__main__":
    test_RemoveDuplicates(ListRemoveDuplicates)
    test_RemoveDuplicates(ListRemoveDuplicatesSets)
   