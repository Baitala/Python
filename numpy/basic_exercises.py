import numpy as np

arr1 = np.array([0, 1, 1, 1]) 
print(arr1)
print(any(arr1))

arr2 = np.array([0, 0, 0, 0]) 
print(arr2)
print(any(arr2))

arr3 = np.array([np.inf, 0, 5, 1.1, np.nan])
print(arr3)
print(any(arr3))
print(np.isfinite(arr3))

num1 = 10
num2 = 9.1
num3 = 8
print(np.allclose([num1],[num2]))
print(np.allclose([num1],[num3]))



