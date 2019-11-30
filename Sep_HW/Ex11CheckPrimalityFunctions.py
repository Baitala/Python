# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no 
# divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

def is_prime(user_number):
    """The function take an number and defines it is prime or not, returns 
    boolean"""
    
    flag_prime = True
    if user_number <= 0:
        return False
    
    for i in range(2, user_number):
        if user_number % i != 0:
            continue
        elif user_number % i == 0:
            flag_prime = False
        else:
            raise ValueError
    return flag_prime


if __name__ == "__main__":
    print("Pass1" if is_prime(1) == True else "Error1")
    print("Pass2" if is_prime(2) == True else "Error2")
    print("Pass3" if is_prime(3) == True else "Error3")
    print("Pass4" if is_prime(4) == False else "Error4")
    print("Pass5" if is_prime(5) == True else "Error5")
    print("Pass6" if is_prime(0) == False else "Error6")
    print("Pass7" if is_prime(-1) == False else "Error7")
    print("Pass8" if is_prime(4999) == True else "Error8")
    
    try:
        is_prime("Fdd")
    except TypeError:
        print("Pass9")
    except:
        print("Error9 other")
    else:
        print("Error9")