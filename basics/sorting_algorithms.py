'''Trying out different sorting algorithms:
1. Insert sort
2. Choise sort
3. Bubble sort
4. Count sort
5. Merge sort
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

def merge(A:list, B:list):
    '''stable merge sort of two sorted arrays A and B
    from lecture #9
    https://www.youtube.com/watch?v=qf82-r9hl2Y&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=9'''

    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] < B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    '''stable merge sort array A
    from lecture #9
    https://www.youtube.com/watch?v=qf82-r9hl2Y&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=9'''
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(A)):
        A[i] = C[i]

def hoar_sort(A):
    '''Hoar (quick) sort of array A
    from lecture #9
    https://www.youtube.com/watch?v=qf82-r9hl2Y&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=9'''
    if len(A) <= 1:
        return
    L = []
    M = []
    R = []
    barrier = A[0]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

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
    sorting_algorithm(num)
    print("TC2", "Passed" if num == num_sorted else "Failed")

def test_sort_TC3(sorting_algorithm):
    '''Basic repeating numbers TC'''
    num = [4, 5, 4, 3, 5, 2, 2, 1, 3, 1]
    num_sorted = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    sorting_algorithm(num)
    print("TC3", "Passed" if num == num_sorted else "Failed")

def test_sort_TC4(sorting_algorithm):
    '''All numbers in list are same.'''
    num = [1] * 100
    num_sorted = [1] * 100
    sorting_algorithm(num)
    print("TC4", "Passed" if num == num_sorted else "Failed")

def test_sort_TC5(sorting_algorithm):
    '''Data already sorted'''
    num = list(range(101))
    num_sorted = list(range(101))
    sorting_algorithm(num)
    print("TC5", "Passed" if num == num_sorted else "Failed")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
    test_sort(count_sort)
    test_sort(merge_sort)
    test_sort(hoar_sort)


