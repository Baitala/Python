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
    test_second_max_TC6(secmax)
    test_second_max_TC7(secmax)
    
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

def test_second_max_TC6(secmax):
    #cycling through many genearated arrays
    TC_Passed = True
    for num in range(100):
        if secmax([num] * 10 + [num + 1] * 10) != num:
            TC_Passed = False
    print("TC6:", "Passed" if TC_Passed else "Failed")

def test_second_max_TC7(secmax):
    #cycling through many randomly genearated arrays
    TC_Passed = True
    for num in range(100):
        #generating test array
        A = [0] * randint(10, 100)
        for i in range(len(A)):
            A[i] = randint(1,1000)
        max2_position = max_position = randint(0,len(A)-1)
        #genearting second maximum position not matching max pos
        while max2_position == max_position:
            max2_position = randint(0,len(A)-1)    
        A[max_position] = 1000
        A[max2_position] = max2 = 999
		#testing
        if secmax(A) != max2:
            TC_Passed = False
    print("TC7:", "Passed" if TC_Passed else "Failed")

if __name__ == "__main__":
    test_second_max(second_max)
