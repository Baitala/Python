# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or 
# exactly right. (Hint: remember to use the user input lessons from the very 
# first exercise)

# Extras:

#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends,
#  print this out.


import random


def guessing_game(guess_number):
# """The function should randomly generate a sected number in range from 1 to 9,
# and return one of three results:
# 'You guessed it' in case you guess the number,
# 'Too high' in case your number is bigger then the generated,
# 'Too low' if your number is smaller then the generated.
# """

    secret_number = random.randint(1, 9)

    if guess_number == "exit":
        quit
    elif guess_number == secret_number:
        return "You guessed it!"
    elif guess_number > secret_number:
        return "Too high."
    elif guess_number < secret_number:
        return "Too low."






    
# print("You have guessed " +  + " times!!!")

if __name__ == "__main__":
    secret_number = 5
    # print ("Pass 1" if guessing_game("exit") else "Error1")
    print("Pass2" if guessing_game(4) == "Too low." else "Error2")
    print("Pass3" if guessing_game(6) == "Too high." else "Error3")
    print("Pass4" if guessing_game(5) == "You guessed it!" else "Error4")
    
