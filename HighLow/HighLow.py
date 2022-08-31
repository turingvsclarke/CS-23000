# Create an interactive game that prompts the user to guess a random number and gets them to guess the number
# by telling them whether their guess was an overestimate or underestimate

# We import the random library

import random

# We begin by getting a random number

secret_number = random.randint(1,100)

# We now ask the user for an integer input

guess = int(input("Please guess a number between 1 and 100.\n"))

# We will keep prompting the user if they didn't guess the number correctly

while guess!=secret_number:

    # If the guess was higher than the correct number we run a certain procedure

    if guess > secret_number:

        # We tell the user the guess was too high and prompt them to make a new guess

        guess = int(input("Your guess is a little too high. Please guess again. You know the drill: 1 to 100.\n"))

    # If the guess was lower than the correct number we run a different certain procedure

    elif guess < secret_number:

        # We tell the user the guess was too low and prompt them to make a new guess

        guess = int(input("Your guess is a little too low. Please guess again. You know the drill: 1 to 100.\n"))

# We congratulate the user if they guess the number correctly

print("Congratulations! You guessed the secret number!")
