'''Binary search from lecture #9
'''

def binary_search(search_list, what_to_find):
    def left_bound(arr, key):
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] < key:
                left = middle
            else:
                right = middle
    return left

    def right_bound(arr, key):
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] <= key:
                left = middle
            else:
                right = middle
    return right
    



if __name__ == "__main__":
    pass 