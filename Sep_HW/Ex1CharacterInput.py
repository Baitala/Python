# Create a program that asks the user to enter their name and their age. Print out a message addressed
#  to them that tells them the year that they will turn 100 years old.

# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many
# copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is 
# the same as pressing the ENTER button)
from datetime import datetime

def CharInput(inname,inage,incycles=1):
    CurrentYear = datetime.now()
    HundredYear = str(CurrentYear.year - inage + 100)
    HundredYearText = inname + ", you'll be a hundred years old in " + HundredYear

    
    i = 0
    while i < incycles:
        print(HundredYearText)
        i += 1





if __name__ == "__main__":
    print("Pass1" if CharInput("Petro",31)=="Petro you'll be a hundred years old in 2088" else "Error1")
    print("Pass2" if CharInput("Petro",31,2)=="""Petro you'll be a hundred years old in 2088 
    Petro you'll be a hundred years old in 2088""" else "Error2")



    