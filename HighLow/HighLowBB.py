# A program that allows the user to pick a number and guesses that number based on commands from the user
# Future version should allow the user to choose to be the one guessing or the one choosing
# Future version should handle exceptions if the upper bound and lower bound become the same
# import the random library to allow generation of random numbers

import random

class Guessing_Game:

    # Starts the game by deciding what 

    def start_game(self):

        # Ask the user to provide an acceptable upper bound and lower bound

        print("Welcome to the guessing game! Please provide the range of numbers to be guessed from today!")

        keepgoing = True

        # Input numbers to assign to the bounds of the range, assign them to integers, and create exceptions if the bounds don't make sense.

        while keepgoing:

            # Set keepgoing to false so that it will leave the loop if there is no error

            keepgoing = False

            # Try to get integer input from the user about the range of numbers to pick from

            try:
                
                (lower_bound,upper_bound)=(int(input("Lower Bound:\n")),int(input("Upper Bound:\n")))

                # Generate a value with these numbers to make sure they define a valid interval

                random_number = random.randint(lower_bound,upper_bound) 

            # Name error exception if the bounds don't allow for finding a number between them

            except NameError:

        
                keepgoing = True

                print("I'm sorry, that range doesn't make sense. Please make sure that the upper bound is the bigger number.")

            # Value error exception if the user didn't actually input an integer

            except ValueError:

                keepgoing = True

                print("I'm sorry, that didn't seem like an integer to me. Please try to enter the range again.")

        return(upper_bound,lower_bound,random_number)

    # The choosing a number option

    def choosing(self,upper_bound,lower_bound,random_number):

        # Create a dictionary, pairing key commands with high, low, and correct

        controls = {"correct":"c","too high":"h","too low":"l"}

        # Tell the user each key command

        # Begin the guessing process

        print("I'm going to start guessing now. Is",guess,"correct? Let me know using the correct key commands.")

        # Capitalize the user's input just in case they're lazy

        feedback = input().capitalize()

        # Loop different responses as long as the user doesn't say the word for correct

        wrong_guess = True

        while wrong_guess:

            # If the user inputs the prompt for too low, change the lower bound for the acceptable range and generate a new guess

            if feedback == "L":

                # Let the lower bound be the previous guess

                lower_bound = guess+1

                # Generate a new number within the acceptable range

                guess = random.randint(lower_bound,upper_bound-1)

                # Tell the user the new guess and ask if that's correct

                print("Is",guess,"correct? Let me know using the correct key commands.")

                feedback = input().capitalize()

            # If the user said the prompt for too high, change the upper bound for the acceptable range and generate a new guess

            elif feedback == "H":

                # Let the upper bound be the previous guess

                upper_bound = guess-1

                # Generate a new number within the acceptable range

                guess = random.randint(lower_bound,upper_bound)

                # Tell the user of the new guess and ask if that's correct

                print("Is",guess,"correct? Let me know using the correct key commands.")

                feedback = input().capitalize()

            elif feedback == "C":

                # If the user said the answer was correct, print out a message reflecting computer's excitement and end the guessing process

                print("Oh ya! I guessed it! Woohoo! Wooho!\n I nailed it, aww, aww, I'm so incredible.\n Gloat, gloat, etcetera, etcetera.")

                wrong_guess = False
            
            # Since these are the only acceptable inputs, let the user that their input was unacceptable

            else:

                print("I'm sorry, that's not a valid command. Here are the acceptable commands to indicate if my guess is correct:")

                feedback = input().capitalize

                # If the user ever says that one number is too low while the one after it is too high, 

                ##if upper_bound == lower_bound + 1:

                ##  print("hi")

    # The guessing a number option

    def guessing(self,upper_bound,lower_bound,random_number):
            
        # We begin by having a secret number

        secret_number = random_number

        # We ask the user for an integer input

        guess = int(input("Please guess a number between " + str(upper_bound) + "and " + str(lower_bound) + ".\n"))

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

# Ask the user if they want to guess a number, choose a number, or quit

choice = input("Hi! Welcome to the guessing game! You can either choose a secret number or guess a secret number. Enter 'g' to guess, 'c' to choose, or 'q' to quit.\n").capitalize()

# Begin the game

playing = True

new_game = Guessing_Game()

while playing:

    if choice == "G":

        (x,y,z) = new_game.start_game()

        new_game.guessing(x,y,z)

    elif choice == "C":

        (x,y,z) = new_game.start_game()

        new_game.choosing(x,y,z)

    elif choice == "Q":

        print("Thanks for playing.\nGoodbye.")

        playing = False

    else:

        choice = input("Sorry I don't understand. Enter 'g' to guess a secret number, 'c' to choose a secret number, and 'q' to quit the game.\n").capitalize()

