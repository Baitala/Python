import heapq

def test_heap():
    test_array1 = [3, 5, 7, 1, 2, 4, 6, 3, 5, 8, 10, 1, 2]
    print("First array:", test_array1)
    heapq.heapify(test_array1)
    print("First heap:", test_array1)
    heapq.heappush(test_array1, 100)
    print("First heap + 100:", test_array1)
    var1 = heapq.heappop(test_array1)
    print("First heap - 1:", test_array1)
    heapq.heappush(test_array1, 0)
    print("First heap + 0:", test_array1)
    heapq.heappush(test_array1, 5)
    print("First heap + 5:", test_array1)

    test_array2 = list(range(10))
    print("Sec array:", test_array2)
    heapq.heapify(test_array2)
    print("Sec heap:", test_array2)

    merged_list = heapq.merge(test_array1, test_array2)
    print("Merged: ", list(merged_list))
    

if __name__ == "__main__":
    test_heap()
