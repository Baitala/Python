import asyncio

def merge_sort(numbers):
    N = len(numbers)
    half = N // 2
    first_half = numbers[0:half]
    second_half = numbers[half:N]

    async def sort_part_of_list(arr):
        '''Got this from 
        https://www.geeksforgeeks.org/python-program-for-bubble-sort/'''
        n = len(arr)
 
        # Traverse through all array elements
        for i in range(n):
    
            # Last i elements are already in place
            for j in range(0, n-i-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def merge_lists(numlist1, numlist2):
        '''Merges two sorted lists
        Check it for stability of algorithm 
        https://www.wikidata.org/wiki/Q11450547'''
        sorted_list = []
        len1 = len(numlist1)
        len2 = len(numlist2)
        i = 0
        j = 0
        while i < len1 and j < len2:
            #print(i, j, '\t', numlist1[i], numlist2[j])
            if numlist1[i] <= numlist2[j]:
                sorted_list.append(numlist1[i])
                i += 1
            else:
                sorted_list.append(numlist2[j])
                j += 1
        if i < len1:
            sorted_list += numlist1[i:len1]
        return sorted_list


    async def parallel_sorting():
        await asyncio.gather(
            sort_part_of_list(first_half),
            sort_part_of_list(second_half)
        )
    
    asyncio.run(parallel_sorting())
    sorted_numbers = merge_lists(first_half, second_half)
    numbers[0:N] = sorted_numbers


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
    num = list(range(101))
    num_sorted = list(range(101))
    sorting_algorithm(num)
    print("TC5", "Passed" if num == num_sorted else "Failed")

if __name__ == "__main__":
    test_sort(merge_sort)
