# A program that allows the user to pick a number and guesses that number based on commands from the user
# Future version should allow the user to choose to be the one guessing or the one choosing
# Future version should allow the user to determine the range of numbers to be played with
# Future version should handle exceptions if the upper bound and lower bound become the same
# See if there's a way to handle integers more efficiently within inputs
# import the random library to allow generation of random numbers

import random

# Ask the user to provide an acceptable upper bound and lower bound

print("Welcome to the guessing game! Please provide the range of numbers to be guessed from today!")

# Convert these values to integers and create an exception for a value error

(lower_bound,upper_bound)=(int(input("Lower Bound:\n")),int(input("Upper Bound:\n")))

# Value error exception

# Create a dictionary, pairing key commands with high, low, and correct

# Tell the user the rules, specifically each key command corresponding to high, low, and correct and the range that was chosen

# Print out the initial guess by randomly generating a number between the upper and lower bounds

guess = random.randint(lower_bound-1,upper_bound+1)

print("Is",guess,"correct? Let me know using the correct key commands.")

feedback = input()

# Loop different responses as long as the user doesn't say the word for correct

while feedback.capitalize()!="C":

# Check to make sure user feedback about the guess is acceptable by checking that it is within the list of acceptable options

    # If the user inputs the prompt for too low, change the lower bound for the acceptable range and generate a new guess

    if feedback.capitalize() == "L":

        # Let the lower bound be the previous guess

        lower_bound = guess

        # Generate a new number within the acceptable range

        guess = random.randint(lower_bound,upper_bound)

        # Tell the user the new guess and ask if that's correct

        print("Is",guess,"correct? Let me know using the correct key commands.")

        feedback = input()

    # If the user said the prompt for too high, change the upper bound for the acceptable range and generate a new guess

    elif feedback.capitalize() == "H":

        # Let the upper bound be the previous guess

        upper_bound = guess

        # Generate a new number within the acceptable range

        guess = random.randint(lower_bound,upper_bound)

        # Tell the user of the new guess and ask if that's correct

        print("Is",guess,"correct? Let me know using the correct key commands.")

        feedback = input()

# If the while loop was passed, the user said the answer was correct, so print out a message reflecting computer's excitement

print("Oh ya! I guessed it! Woohoo! Wooho!\n I nailed it, aww, aww, I'm so incredible.\n Gloat, gloat, etcetera, etcetera.")