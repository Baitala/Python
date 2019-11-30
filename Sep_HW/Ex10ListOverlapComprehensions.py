# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program 
# works on two lists of different sizes. Write this in one line of Python using
# at least one list comprehension.
# 
# Extra:

#   Randomly generate two lists to test this

class custom_list:
    def __init__(self, inlist):
        self.internal_list = inlist
    def __mod__(self, other_custom_list):
        '''The method overloads % operation to return the list of unique
        common elements'''
        list_common = [number for number in self.internal_list if number in other_custom_list.internal_list]
        unique_list = []
        for number in list_common:
            if number not in unique_list:
                unique_list.append(number)
            else:
                continue
        return unique_list




def list_common(list1, list2):
    '''The function takes two lists and returns a list of common elements'''
    list_common = [number for number in list1 if number in list2]
    unique_list = []
    for number in list_common:
        if number not in unique_list:
            unique_list.append(number)
        else:
            continue
    return unique_list

def list_common_recursive(list1, list2):
    '''The function takes two lists and returns a list of common elements'''




if __name__ == "__main__":
    
    a = [1, 1, 2, 3, 5, 8, 5, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 4, 3, 5]
    print("Pass1" if list_common(a,b) == [1,2,3,5,8,13] else "Error1")
 