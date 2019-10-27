# Ask the user for a string and print out whether this string is a palindrome 
#or not. (A palindrome is a string that reads the same forwards and backwards.)

def IsPalindromeList(intext):
    """
    """
    inlist = [x for x in intext]
    print(inlist)
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


if __name__ == "__main__":
    print("Pass1" if IsPalindromeList("ALLA") else "Error1")
    print("Pass2" if IsPalindromeList("ALTETLA") else "Error2")
    print("Pass1" if IsPalindromeList("AlLa") else "Error1")
    