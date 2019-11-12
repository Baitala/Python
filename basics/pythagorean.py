'''Given three integer numbers, determine 
whether it’s a Pythagorean triple or not'''

from random import randint

def is_Pythagorean_triple(a: int, b: int, c: int):
    '''If three integer numbers a, b, c are solution to 
    a**2 + b**2 = c**2
    if yes - returns True
    if no - returns False'''

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError

    biggest_number_index = [a, b, c].index(max([a, b, c]))
    if __debug__: 
        print(a, b, c)
        print(biggest_number_index)
    if biggest_number_index == 0:
        expression = b**2 + c**2 - a**2
        if __debug__: print(c**2 + b**2, a**2)
    elif biggest_number_index == 1:
        expression = a**2 + c**2 - b**2
        if __debug__: print(a**2 + c**2, b**2)
    elif biggest_number_index == 2:
        expression = a**2 + b**2 - c**2
        if __debug__: print(a**2 + b**2, c**2)
    else:
        raise AssertionError("Something went wrong")

    if __debug__: print(expression)
    if expression == 0:
        return True
    elif expression != 0:
        return False
    else:
        raise ValueError

def test_is_Pythagorean_triple():
    '''Test cases:
    [3, 4, 5]
    [4, 5, 3]
    [5, 3, 4]
    [3, 5, 4]
    [5, 4, 3]
    [4, 3, 5]'''
    test1_is_Pythagorean_triple()
    test2_is_Pythagorean_triple()
    test3_is_Pythagorean_triple()
    test4_is_Pythagorean_triple()
    test5_is_Pythagorean_triple()
    test6_is_Pythagorean_triple()
    test7_is_Pythagorean_triple()

def test1_is_Pythagorean_triple():
    x, y, z = 3, 4, 5
    print("TC1", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test2_is_Pythagorean_triple():
    x, y, z = 4, 5, 3
    print("TC2", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test3_is_Pythagorean_triple():
    x, y, z = 5, 3, 4
    print("TC3", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test4_is_Pythagorean_triple():
    x, y, z = 3, 5, 4
    print("TC4", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test5_is_Pythagorean_triple():
    x, y, z = 5, 4, 3
    print("TC5", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test6_is_Pythagorean_triple():
    x, y, z = 4, 3, 5
    print("TC6", "Passed" if is_Pythagorean_triple(x, y, z) else "Failed")

def test7_is_Pythagorean_triple():
    '''Testing negative and zero values'''
    i = 0
    N = 1000
    failed_flag = False
    while i < N:
        x = randint(-10000,0)
        y = randint(-10000,0)
        z = randint(-10000,0)
        i += 1
        try:
            is_Pythagorean_triple(x, y, z)
        except ValueError:
            pass
        except:
            failed_flag = True
        
    print("TC7 Failed" if failed_flag else "TC7 Passed")

if __name__ == "__main__":
    test_is_Pythagorean_triple()
