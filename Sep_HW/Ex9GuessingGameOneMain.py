# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
#  guess the number, then tell them whether they guessed too low, too high, or 
# exactly right. (Hint: remember to use the user input lessons from the very 
# first exercise)

# Extras:

#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends,
#  print this out.
from Ex9GuessingGameOne import guessing_game

user_number = int(input("Please, enter your secret number option: "))

return (guessing_game(user_number))