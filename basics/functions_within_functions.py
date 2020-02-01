#function within function

def multiply_by_n(n):
    def multiply(base):
        return base * n
    return multiply

if __name__ == "__main__":
    multiply_by_3 = multiply_by_n(3)
    multiply_by_5 = multiply_by_n(5)
    print(multiply_by_3(2))
    print(multiply_by_5(2))
