# Ask the user for a string and print out whether this string is a palindrome 
#or not. (A palindrome is a string that reads the same forwards and backwards.)

def IsPalindromeList(intext):
    """The function takes a string, makes it lowercase turns it in list and 
    defines if it is a polindrom. It turns True in case if it is and False in 
    opposite sittuation.
    """
    intextl = intext.lower()
    inlist = [x for x in intextl]
    length = len(intext)-1
    half_length = length//2
    
    for i in range(0,half_length,1):
        if inlist[i] == inlist[length-i]:
            continue
        elif inlist[i] != inlist[length-i]:
            return False
        else:
            print("Something went wrong")
    return True

def IsPalindromeStr(intext):
    """The function takes a string, makes it lowercase and defines if it is a 
    polindrom. It turns True in case if it is and False in opposite sittuation.
    """
    intextl = intext.lower()
    # print(intext)
    # print(intextl)
    length = len(intextl)-1
    half_length = length//2
    # print(length)
    # print(half_length)

    for i in range(0,half_length,1):
        if intextl[i] == intextl[length-i]:
            continue
        elif intextl[i] != intextl[length-i]:
            print(i)
            return False
        else:
            print("Something went wrong str")
    return True




if __name__ == "__main__":
    print("Pass1" if IsPalindromeList("ALLA") else "Error1")
    print("Pass2" if IsPalindromeList("ALTETLA") else "Error2")
    print("Pass3" if IsPalindromeList("AlLa") else "Error3")
    print("Pass4" if IsPalindromeList("1234%^&  &^%4321") else "Error4")
    print("Pass5" if IsPalindromeList("") else "Error5")
    print("Pass1.1" if IsPalindromeStr("ALLA") else "Error1.1")
    print("Pass2.1" if IsPalindromeStr("ALTETLA") else "Error2.1")
    print("Pass3.1" if IsPalindromeStr("AlLa") else "Error3.1")
    print("Pass4.1" if IsPalindromeStr("1234%^&  &^%4321") else "Error4.1")
    print("Pass5.1" if IsPalindromeStr("") else "Error5.1")
    