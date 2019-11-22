import asyncio

def merge_sort(numbers):
    N = len(numbers)
    half = N // 2

    async def sort_part_of_list(numlist):
        pass

    def merge_lists(numlist1, numlist2):
        pass

    async def parallel_sorting():
        await asyncio.gather(
            sort_part_of_list(numbers[0:half]),
            sort_part_of_list(numbers[half:N])
        )
    
    asyncio.run(parallel_sorting())
    merge_lists(numbers[0:half],numbers[half:N])


def test_sort(sorting_algorithm):
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
    num = range(101)
    num_sorted = range(101)
    sorting_algorithm(num)
    print("TC5", "Passed" if num == num_sorted else "Failed")

if __name__ == "__main__":
    test_sort(merge_sort)
