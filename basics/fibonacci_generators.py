'''making fibonacci generators'''
def fibonacci_cycle(nth: int) -> int:
    '''nth Fibonacci number, with cycles logic'''
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    for i in range(2,nth+1):
        fibonacci_cur = fib_n_minus_2 + fib_n_minus_1
        #shifting prevoius two values to new position
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fibonacci_cur
        yield fibonacci_cur

def fibonacci_list(nth: int) -> int:
    '''nth Fibonacci number, with cycles logic, filling array first'''
    Fibonaccis = [0, 1]
    for i in range(2,nth+1):
        Fibonaccis += [Fibonaccis[i-1] + Fibonaccis[i-2]]
        yield Fibonaccis[i]

for f in fibonacci_list(10):
    print(f)

for fib in fibonacci_cycle(10):
    print(fib)

A = list(range(100))
B = [A[i]**2 for i in fibonacci_cycle(10)]
print(B)
