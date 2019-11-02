# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using 
# input), compare them, print out a message of congratulations to the winner, and
# ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
from Ex8WellPaperScissors import *

print("""Plese enter your choice W for Well, P for Paper and S for scissors. 
Let's start!""") #Rock or R and so on

P1 = input("Player 1 plese enter you choise: ")

P2 = input("Player 2 plese enter you choise: ")

print(WellPaperScissors(P1, P2))