# Eli.SK
# random number guess HW
#Aug 28, 2024

#instructions
#error handling
#random number 1 - 1000
#user guess higher or lower until the number is found
#pack everythign into a function
#once game over prompt for play again
#push to git and turn in

import random

def play_game():
    # Generate a random number between 1 and 1000
    number_to_guess = random.randint(1, 1000)

    # Initialize the number of attempts
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")

    while True:
        # Ask the user for their guess
        while True:
            try:
                user_guess = int(input("Guess a number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Increment the number of attempts
        attempts += 1

        # Check if the user's guess is correct
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        # Check if the user's guess is too high
        elif user_guess > number_to_guess:
            print("Too high. Try again!")
        # Check if the user's guess is too low
        else:
            print("Too low. Try again!")

while True:
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            break
        elif play_again.lower() == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")