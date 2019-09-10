"""
Making function for defining max value in the list.
"""

def maxOfList(inlist):
    max = inlist[1]
    for x in inlist:
        if x > max:
            max = x
    return max   


if __name__=="__main__":
    l = [9, 1, -2, 9, 5, 9, 4, 9]
    print ("Pass1" if maxOfList(l) == 9 else "Error1")