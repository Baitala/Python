# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:

#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one\
# number to divide by (check). If check divides evenly into num, tell that to 
# the user. If not, print a different appropriate message.

def OddOrEven(innumber):
    """Returns appropriate conclusion is the number Odd or Even
    """

    if innumber%2 == 0:
        return "The number is even"
    elif innumber%2 != 0:
        return "The number is odd"
    else:
        raise ValueError


if __name__ == "__main__":
    print("Pass1" if OddOrEven(4)=="The number is even" else "Error1")
    print("Pass2" if OddOrEven(3)=="The number is odd" else "Error2")
    print("Pass3" if OddOrEven(-4)=="The number is even" else "Error3")
    print("Pass4" if OddOrEven(-3)=="The number is odd" else "Error4")
    print("Pass5" if OddOrEven(0)=="The number is even" else "Error5")
    #print("Pass6" if OddOrEven("sklfjaklfa")==ValueError else "Error6")
    try:
        OddOrEven("jlksjdfklsdf")
    except ValueError:
        print("Pass6")
    except:
        print("Pass6")
    else:
        print("Error6.1")