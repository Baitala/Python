from Ex9GuessingGameOOP import Guessing_Game

current_game = Guessing_Game()
user_number = 0

trigger = "continue"

while user_number != current_game.secret_number and user_number != "exit":
    user_number = int(input("Please enter your number: "))
    print(current_game.guess(user_number))