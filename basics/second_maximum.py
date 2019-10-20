def all_numbers_equal(array_of_numbers):
    '''Checks if all elements in an array are same values.
    Returns True if yes
    Returns False if values are not equal.
    E.g.: [1, 1, 1, 1] -> True
    [2, 2, 2, 1] -> False'''
    value = array_of_numbers[0]
    for i in range(1,len(array_of_numbers),1):
        if value != array_of_numbers[i]:
            return False
    return True

def test_all_numbers_equal():
    arr1 = [1, 1, 1]
    arr2 = [1, 1, 2]
    if all_numbers_equal(arr1):
        print("1: passed")
    else:
        print("1: failed")
    
    if not all_numbers_equal(arr2):
        print("2: passed")
    else:
        print("2: failed")

def second_max(numbers):
    '''Returns second maximum value of an array;
    If array is less than 2 elements long,
    or has all values equal then returns None'''
    if numbers == [] or len(numbers) <= 2 or all_numbers_equal(numbers):
        return None
    
    max1 = max2 = numbers[0]
    for i in range(1, len(numbers)-1, 1):
        if max1 < numbers[i]:
            max1 = numbers[i]
        if max2 < numbers[i] or max2 >= max1:
            max2 = numbers[i]
    
    return max2



def test_second_max():
    '''Run all autotest for second_max()'''
    test_second_max_TC1()
    test_second_max_TC2()
    test_second_max_TC3()
    test_second_max_TC4()
    test_second_max_TC5()
    test_second_max_TC6()

def test_second_max_TC1():
    '''TC1: Ascending array'''
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if second_max(arr) != 9:
        print("TC1 failed")
    else:
        print("TC1 passed.")

def test_second_max_TC2():
    '''TC2: Descending array'''
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if second_max(arr) != 9:
        print("TC2 failed")
    else:
        print("TC2 passed.")

def test_second_max_TC3():
    '''TC3: Generic array'''
    arr = [1, 3, 6, 10, 5, 3, 8, 9, 6, 1, 2]
    if second_max(arr) != 9:
        print("TC3 failed")
    else:
        print("TC3 passed.")

def test_second_max_TC4():
    '''TC4: Empty array'''
    arr = []
    if second_max(arr) is None:
        print("TC4 passed.")
    else:
        print("TC4 failed")

def test_second_max_TC5():
    '''Array with same values'''
    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    if second_max(arr) is None:
        print("TC5 passed.")
    else:
        print("TC5 failed")

def test_second_max_TC6():
    '''Array with single value'''
    arr = [10]
    if second_max(arr) is None:
        print("TC6 passed.")
    else:
        print("TC6 failed")

if __name__ == "__main__":
    test_second_max()
    test_all_numbers_equal()
    arr = [1, 2, 3]
    print(second_max(arr))