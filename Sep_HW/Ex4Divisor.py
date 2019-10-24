# Create a program that asks the user for a number and then prints out a list of 
# all the divisors of that number. (If you don’t know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor of
# 26 because 26 / 13 has no remainder.)


def MyDivisor(innumber):
    """The function takes a number and return a list of all the divisors of the
    number.
    """
    n_list=[]
        
    for i in range(1,innumber+1,1):
        if innumber%i==0:
            n_list.append(i)
        elif innumber%i!=0:
            continue
        else:
            raise ValueError
    return (n_list)


if __name__ == "__main__":
    print("Pass1" if MyDivisor(4)==[1,2,4] else "Error1")
    print("Pass2" if MyDivisor(1)==[1] else "Error2")
    print("Pass3" if MyDivisor(7)==[1,7] else "Error3")