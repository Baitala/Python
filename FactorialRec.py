
def factorial(quantity):
    '''The function takes an int and calculates factorial for the number'''
    if quantity == 1:
        return 1
    return factorial(quantity-1)*quantity

print(factorial(100))