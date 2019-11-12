#finding second maximal value
from random import randint
import inspect

def second_max(numbers):
    '''Finding second biggest number in array'''
    N = len(numbers)
    max = numbers[0]
    are_all_equal = True
    for i in range(1, N):
        if numbers[i] > max:
            max = numbers[i]
            are_all_equal = False
        elif are_all_equal and numbers[i] < max:
            are_all_equal = False
    if are_all_equal:
        return None
    max2 = numbers[0]
    for i in range(1, N):
        if numbers[i] != max and (numbers[i] > max2 or max2 == max):
            max2 = numbers[i]
    return max2
    

def test_second_max(secmax):
    print("Testing",secmax.__name__ + "():",secmax.__doc__)
    test_second_max_TC1(secmax)
    test_second_max_TC2(secmax)
    test_second_max_TC3(secmax)
    test_second_max_TC4(secmax)
    test_second_max_TC5(secmax)
    
def test_second_max_TC1(secmax):
    #ascending sequence
    A = range(101)
    max2 = 99
    print("TC1:", "Passed" if secmax(A) == max2 else "Failed")

def test_second_max_TC2(secmax):
    #descending sequence
    A = range(100,1,-1)
    max2 = 99
    print("TC2:", "Passed" if secmax(A) == max2 else "Failed")

def test_second_max_TC3(secmax):
    #sequence with repetitions
    A = [1, 2, 5, 1, 2, 4, 5, 3, 3]
    max2 = 4
    print("TC3:", "Passed" if secmax(A) == max2 else "Failed")

def test_second_max_TC4(secmax):
    #all zeros
    A = [0] * 100
    max2 = None
    print("TC4:", "Passed" if secmax(A) is max2 else "Failed")

def test_second_max_TC5(secmax):
    #all equal
    rnumber = randint(1,100)
    A = [rnumber] * 100
    max2 = None
    print("TC5:", "Passed" if secmax(A) is max2 else "Failed")

if __name__ == "__main__":
    test_second_max(second_max)
