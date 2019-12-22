

def fib_rec(n):
    if n <=1:
        return n
    return (fib_rec(n-1) + fib_rec(n-2))

print(fib_rec(30))

def fib_dinamic():
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

#set of algorithm of dinamic programming

def traj_num(N):
    '''Counting number of different routs to some n value'''
    K = [0, 1] + [0] * N
    for i in range (2, N+1):
        K[i] = K[i-2] + K[i-1]
    return K[N]

def count_trajectories(N, allowed:list):
    K = [0, 1, int(allowed[2] + [0] * (N-3)
    for i in range(3, N+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]

#minimal costs of reaching the N 
def connt_min_cost(N, price:list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0]*(n-2)
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]