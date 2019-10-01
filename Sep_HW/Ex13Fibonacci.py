"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of 
numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def FibonnaciGenerator(quantity):
    flist = [1,1]
    if quantity >= 3:
            i = 2 #kind of big bug, actual length is 2
            while i < int(quantity):
                l = len(flist)
                #print(flist) #only for debugging
                flist.append(flist[l-2]+flist[l-1])
                i += 1
            return(flist)
    elif quantity == 1:
        return[1]
    elif quantity == 2:
        return(flist)
    else:
        return("Incorrect input. Please fill number equal or bigger then 1.")



if __name__ == "__main__":
    print("Pass1" if FibonnaciGenerator(10)==[1, 1, 2, 3, 5, 8, 13, 21, 34, 55] else "Error1")
    print("Pass2" if FibonnaciGenerator(1)==[1] else "Error2")
    print("Pass3" if FibonnaciGenerator(2)==[1, 1] else "Error3")
    print("Pass4" if FibonnaciGenerator(3)==[1, 1, 2] else "Error4")
    print("Pass5" if FibonnaciGenerator(4)==[1, 1, 2, 3] else "Error5")
    print("Pass6" if FibonnaciGenerator(0)=="Incorrect input. Please fill number equal or bigger then 1." else "Error6")
    
    #print(FibonnaciGenerator(9999)) #kind of perfomance test
