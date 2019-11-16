#testing out syntax

A = 1, 2
B = 3, 4
C = 4, 5
Arr = [X[0]**2 for X in (A, B, C) if X[1] % 2 == 0]
print(Arr)
