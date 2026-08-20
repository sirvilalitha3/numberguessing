


# Import the random module
# random module is used to generate random numbers
import random


# Create an empty list
# This list will store all the guesses made by the user
guesses = []


# Function to generate the secret number
def generate_number():

    # randint(1, 100) generates a random number
    # between 1 and 100
    return random.randint(1, 100)


# Function to get a valid guess from the user
def get_guess():

    # Keep asking the user until they enter valid input
    while True:

        try:
            # Take input from the user
            # input() gives us a string
            # int() converts that string into an integer
            guess = int(input("Enter your guess (1-100): "))

            # Check whether the number is between 1 and 100
            if 1 <= guess <= 100:

                # If valid, return the guess
                return guess

            else:
                # If the number is outside the range
                print("Please enter a number between 1 and 100.")

        except ValueError:

            # This runs if the user enters something
            # that cannot be converted into an integer
            #
            # Example:
            # User enters "hello"
            # int("hello") causes ValueError
            #
            # Instead of crashing, we show an error message
            print("Invalid input! Please enter a number.")


# Function that contains the main game
def play_game():

    # Generate a random secret number
    secret_number = generate_number()

    # Display the game instructions
    print("\n Guess the number between 1 and 100!")

    # Keep the game running until the user guesses correctly
    while True:

        # Call get_guess() to get a valid number
        guess = get_guess()

        # Add the user's guess to the list
        guesses.append(guess)

        # Check if the guess is smaller than the secret number
        if guess < secret_number:

            print("Too low! Try again.")

        # Check if the guess is greater than the secret number
        elif guess > secret_number:

            print("Too high! Try again.")

        # If neither condition is true,
        # the guess must be equal to the secret number
        else:

            print("\n dinkachika Correct!")

            # len(guesses) tells us how many guesses
            # the user made
            print(f"You guessed it in {len(guesses)} attempts.")

            # Display all the guesses stored in the list
            print("Your guesses:", guesses)

            # Stop the while loop
            break


# Call the function to start the game
play_game()