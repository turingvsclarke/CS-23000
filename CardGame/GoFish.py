# Create a go fish game
from CardGame import*
import random

# create a function that takes in a number and puts that number in a random spot in the card location list. this will be the assignCard function.

def menu():

    option_numbers = ["1)","2)","3)"]

    options = ["Single player vs CPU","Multiplayer","Quit"]

    print("Main menu:")
    for x in options:

        print("{:<4}{:>8}".format(option_numbers[options.index(x)],x))

    option_number = input("Selection(enter the number of the option you'd like):\n")

    return(option_number)

def Game():
    clearDeck()

    print("Welcome to the game of Go Fish! You're now going to have 7 cards placed in your hand. Good luck!")

    # start the game, assigning seven cards and beginning a game loop
    gameplay = True
    player = 0
    for b in range(8):

        assignCard(PLAYER)
        assignCard(COMP)
        # switch players every turn, meaning every loop switches between players.'''

    while gameplay:
        
        showHand(PLAYER)
        playerguess(player)

        # check to see if there are any matches
        matchcheck()

        # check to see if the player just won the game
        if player not in cardLoc:
            print("{} just won the game!".format(playerName[player].capitalize()))
        else:
            # switch players if the previous player hasn't won yet
            player = (player+1)%2

def matchcheck():

    if 1==1:
        z="hi"

def playerguess(player):
    ## If the player is the user, let them enter a rank to guess. If its the computer's turn, just generate a random number isn't doesn't have
    if playerName[player]=="player":

        x=input("Enter the rank you want to ask for:".format())

    elif playerName[player]=="computer":
    # select a random card
        x=player
        while x==player:
            x=randint(0,51)

    # check all the possible locations for that rank, meaning add 13 three times to the index and check the rank each time
    # if the rank of any suit isn't in the other player's hand, print out go fish
    if cardLoc[rankName.index(x)]!=(player+1)%2:
        print("Go Fish!")
        assignCard(player)

    else:
        y=cardLoc[rankName.index(x)]
        # assign all the cards of that rank to to the player
        while y<51:
    
            cardLoc[y]=player
            y+=13

def main():
    keepgoing = True

    choice = menu()
    while keepgoing:

        if choice == "1":
        
            Game()
        
        elif choice == "2":

            # possible multiplayer option
            hi="hi"

        elif choice == "3":

            print("Goodbye. Thanks for playing.")

            keepgoing=False

        else:

            print("That was not a valid option. Please try again.")

if __name__ == "__main__":

    main()