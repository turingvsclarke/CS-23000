# A program that allows the user to pick a number and guesses that number based on commands from the user
# import the random library to allow generation of random numbers

import random

class Guessing_Game:

    # Starts the game by deciding what range of numbers play will be limited to

    def start_game(self):

        # Ask the user to provide an acceptable upper bound and lower bound

        print("The game is about to start! First, please provide a range of numbers to be guessed from today so this program doesn't run infinitely.")

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

            # Value error exception if the user didn't actually input an integer

            except ValueError or upper_bound == lower_bound:

                keepgoing = True

                print("I'm sorry, that didn't seem like a valid range to me. Please try to enter the integer values again, making sure that the upper bound is the bigger number.")

        return(upper_bound,lower_bound,random_number)

    # The choosing a number option

    def choosing(self,upper_bound,lower_bound,random_number):

        # Create a dictionary pairing key commands with high, low, and correct

        controls = {"correct":"(c)","too high":"(h)","too low":"(l)"}

        # Tell the user each key command

        print("Cool! So I'm going to guess a secret number that you choose.\nReady? First, here are the rules:\nWhen I guess a number, tell me if it is too high, too low, or correct. Indicate these with the following key commands:")

        for key in controls:

            print("{:<12}{:>6}".format(key,controls[key]))

        # Begin the guessing process

        guess = random_number

        print("I'm going to start guessing now. Is",guess,"correct? Let me know using the correct key commands.")

        # Capitalize the user's input just in case they're lazy

        feedback = input().capitalize()

        # Loop different responses as long as the user doesn't say the word for correct

        wrong_guess = True

        while wrong_guess:
            
            # Stop the program if user input indicates that there is an integer between two successive integers

            if upper_bound == lower_bound:

                # Send the user to the correct condition since the range has no integer between it and must be the bounds

                print("Got it! The answer must be " + str(upper_bound) + " or else you cheated and never had a number.")

                feedback = "C"

            # Stop the program if user made the range undefined

            elif upper_bound<lower_bound:

                print("But that means the value is one which doesn't match the provided range or isn't an integer. You must have cheated or made a mistake. So technically I win.")

                wrong_guess = False

            # If the user inputs the prompt for too low, change the lower bound for the acceptable range and generate a new guess

            if feedback == "L":

                # Let the lower bound be greater than the previous guess

                lower_bound = guess+1

                # Only generate a new number if the range is well defined

                if upper_bound>lower_bound:

                    # Generate a new number within the acceptable range

                    guess = random.randint(lower_bound,upper_bound)

                    # Tell the user the new guess and ask if that's correct

                    print("Is",guess,"correct? Let me know using the correct key commands.")

                    feedback = input().capitalize()

            # If the user said the prompt for too high, change the upper bound for the acceptable range and generate a new guess

            elif feedback == "H":

                # Let the upper bound be less than the previous guess

                upper_bound = guess - 1

                # Only generate a new guess if the range is well defined

                if upper_bound>lower_bound:

                    # Generate a new number within the acceptable range

                    guess = random.randint(lower_bound,upper_bound)

                    # Tell the user of the new guess and ask if that's correct

                    print("Is",guess,"correct? Let me know using the correct key commands.")

                    feedback = input().capitalize()

            elif feedback == "C":

                # If the user said the answer was correct, print out a message reflecting computer's excitement and end the guessing process

                print("Oh ya! I guessed it! Woohoo! Wooho!\n I nailed it, aww, aww, I'm so incredible.\n Gloat, gloat, etcetera, etcetera.")

                wrong_guess = False
            
            # Since these are the only acceptable inputs, let the user know that any other input was unacceptable

            else:

                print("I'm sorry, that's not a valid command. Here are the acceptable commands to indicate if my guess is correct:")

                for key in controls:

                    print("{:<12}{:>6}".format(key,controls[key]))

                # Take what is hopefully now correct input

                feedback = input().capitalize()

    # The guessing a number option

    def guessing(self,upper_bound,lower_bound,random_number):
            
        # We begin by having a secret number

        secret_number = random_number

        # We ask the user for an integer input and make sure it is an integer

        not_working = True

        while not_working:
            
            try: 
                
                guess = int(input("Please guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ".\n"))

                not_working = False

            except ValueError:

                print("I'm sorry, that wasn't a value I could understand. Please try again, making sure your guess is an integer in the range you picked.")

                not_working = True

        # We will keep prompting the user if they didn't guess the number correctly

        while guess!=secret_number:

            # If the guess was higher than the correct number we run a certain procedure

            if guess > secret_number:

                # We tell the user the guess was too high and prompt them to make a new guess

                print("Your guess is a little too high. Please guess again. You know the drill: ",lower_bound," to " + str(upper_bound) + ".")

            # If the guess was lower than the correct number we run a different certain procedure

            elif guess < secret_number:

                # We tell the user the guess was too low and prompt them to make a new guess

                print("Your guess is a little too low. Please guess again. You know the drill: ",lower_bound," to " + str(upper_bound) + ".")

            # Get another integer, running an exception to make sure it is an integer

            not_working = True

            while not_working:
                
                try: 
                    
                    guess = int(input())

                    not_working = False

                except ValueError:

                    print("I'm sorry, that wasn't a value I could understand. Please try again, making sure your guess is an integer in the range you picked.")

                    not_working = True

        # We congratulate the user if the loop ended, meaning they guessed the number correctly

        print("Congratulations! You guessed the secret number!")

########## GAME IS BEGUN HERE, EVERYTHING ABOVE IS THE CLASS DEFINING HOW THE GAME RUNS

# Ask the user if they want to guess a number, choose a number, or quit

choice = input("Hi! Welcome to the guessing game! You can either choose a secret number or guess a secret number. Enter 'g' to guess, 'c' to choose, or 'q' to quit.\n").capitalize()

# Begin the game

new_game = Guessing_Game()

# Initiate a menu sequence

playing = True

while playing:

    if choice == "G":

        (x,y,z) = new_game.start_game()

        new_game.guessing(x,y,z)

        choice = input("That was fun!\nYou can now choose to play again or quit the game. Press 'g' to guess a number, 'c' to choose a number, or 'q' to quit.\n").capitalize()

    elif choice == "C":

        (x,y,z) = new_game.start_game()

        new_game.choosing(x,y,z)

        choice = input("That was fun!\nYou can now choose to play again or quit the game. Press 'g' to guess a number, 'c' to choose a number, or 'q' to quit.\n").capitalize()

    elif choice == "Q":

        print("Thanks for playing.\nGoodbye.")

        playing = False

    else:

        choice = input("Sorry I don't understand. Enter 'g' to guess a secret number, 'c' to choose a secret number, and 'q' to quit the game.\n").capitalize()

