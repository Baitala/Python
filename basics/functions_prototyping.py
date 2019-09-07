

def is_even_number(x):
    """ Определяет является ли число простым.
        x - целое положительное число.
        Если простое, возвращает True,
        иначе False.
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return True
        divisor += 1
    return False
