def levenstein (A,B):
    F = [[(i+j) if i*j == 0 else 0 for i in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(1, len((A)+1)):
        for j in range(1, len((B)+1)):
            if A[i-1]==B[j-1]:
                F[i][j]=F[i-1][j-1]
            else:
                F[i][j]=1+min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]

# Перевірка рівності стрічок:
def equal(A,B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

#
def search_substring(s,sub):
    for i in range(0,len(s)-len(sub)):
        if equal(s[i:i+len(sub)],sub):
            print(i)