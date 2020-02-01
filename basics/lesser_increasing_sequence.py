#Наибольшая возрастающая подпоследовательность

def gis(A):
    F = [0] * (len(A)+1)
    for i in range(1, len(A) + 1):
        maximum = 0
        for j in range(0, i):
            if A[i] > A[j] and F[j] > maximum:
                maximum = F[j]
        F[i] = maximum + 1
    return F[len(A)]