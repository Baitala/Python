# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or 
# exactly right. (Hint: remember to use the user input lessons from the very 
# first exercise)

# Extras:

#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends,
#  print this out.
import random

class Guessing_Game:
    """The class should provide realisation of guessing game task.
    """
    def __init__(self):
        """Initializing with generation of secret number.
        """
        self.secret_number = random.randint(1, 9)
        if __name__ == "__main__":
            self.secret_number = 5
    
    def guess(self, guess_number):
        """Accepts user number and compares to secret number. As a result
        it returns string with results of comparing.
        """
        if guess_number == self.secret_number:
            return "You guessed it!"
        elif guess_number > self.secret_number:
            return "Too high."
        elif guess_number < self.secret_number:
            return "Too low."
        else:
            return ValueError


if __name__ == "__main__":
    test_game = Guessing_Game()
    
    print("Pass1" if test_game.guess(5) == "You guessed it!" else "Error1")
    print("Pass2" if test_game.guess(4) == "Too low." else "Error2")
    print("Pass3" if test_game.guess(6) == "Too high." else "Error3")