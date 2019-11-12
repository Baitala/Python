'''Trying out different sorting algorithms:
1. Insert sort
2. Choise sort
3. Bubble sort
4. Count sort
5. ...
'''
def insert_sort(array):
    '''Insert sort'''
    pass

def choise_sort(array):
    '''Choise sort'''
    pass

def bubble_sort(array):
    '''Bubble sort'''
    pass

def count_sort(array):
    '''Count sort'''
    pass

def test_sort(sorting_algorithm):
    '''Testing any sort algorithm by feeding it data and
    checking output. Argument is the name of sorting function
    '''
    print("Testing", sorting_algorithm.__doc__)
    test_sort_TC1(sorting_algorithm)
    test_sort_TC2(sorting_algorithm)
    test_sort_TC3(sorting_algorithm)
    test_sort_TC4(sorting_algorithm)
    test_sort_TC5(sorting_algorithm)


def test_sort_TC1(sorting_algorithm):
    '''Basic TC with [1,...5] array'''
    num = [4, 5, 2, 3, 1]
    num_sorted = [1, 2, 3, 4, 5]
    sorting_algorithm(num)
    print("TC1", "Passed" if num == num_sorted else "Failed")

def test_sort_TC2(sorting_algorithm):
    '''TC with pre-mixed slices of arrays'''
    num = list(range(90,100)) + list(range(50,90)) + list(range(50))
    num_sorted = list(range(100))
    print("TC2", "Passed" if num == num_sorted else "Failed")

def test_sort_TC3(sorting_algorithm):
    '''Basic repeating numbers TC'''
    num = [4, 5, 4, 3, 5, 2, 2, 1, 3, 1]
    num_sorted = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    print("TC3", "Passed" if num == num_sorted else "Failed")

def test_sort_TC4(sorting_algorithm):
    pass

def test_sort_TC5(sorting_algorithm):
    pass

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
    test_sort(count_sort)


