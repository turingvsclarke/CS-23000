import random

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

# create a clear deck function that 

def clearDeck():

  cardLoc = [0] * NUMCARDS

# create a function that takes in a number and puts that number in a random spot in the card location list. this will be the assignCard function.

def assignCard(self):

  # Pick a random card out of 52 cards

  card = random.randint(0,len(cardLoc)-1)

  # If that card already has that player value, pick another random number so we aren't just assigning the player to the same card multiple times

  while cardLoc[card] == self:

    card = random.randint(0,len(cardLoc)-1)

  # Change the value at that random space of cardLoc to whatever the player's number is

  cardLoc[card] = self

# create a function that takes no input but prints out each card and its location in the game

def showDeck():

  print("Location of all cards:")

  # Print out a nice header labelling columns to show the location in the deck, the value of the card, and the player to which it belongs 
  # It should be justified so that it is right above the location of the deck

  print("{:<9}{:<14}{:<10}".format("#","card","location"))

  x=0

  for i in range(len(cardLoc)):

    # The loop will find three values: the player, the rank, and the suit

    # It will print the player, mainly the value of the playerName string at x

    player = playerName[cardLoc[x]]

    # The card's rank will be the value of the rankName at the index y modulus 13

    rank = rankName[x%13]

    # The suit will be the value of the suitName at the index y divided by 13 converted to an integer

    suit = suitName[int(x/13)]

    # Print out which card it is, of what rank, and of what suit all neatly left formatted

    print("{:<4}{:<20}{:<20}".format(x,rank + " of " + suit,player))

    x+=1

    # This function will probably be built on a while loop. The key thing when mapping cards to suit and rank is that which cards are where in the card location list is fixed
    # so the real problem is how to map each of 52 cards to the name and rank lists (use modular operator)
    # We can take the modulus of four, returning which rank it is. Rounding the division by four will tell us which suit it is in
    
# create a clear deck function that sets all of the values in the cardlocation array to zero

def clearDeck():

  cardLoc = [0] * NUMCARDS

# Create another function that inputs a number and prints out all the cards corresponding to all the instances of that number in the card location string

def showHand(self):

  # First print out which hand we are displaying

  print("Displaying {} hand:".format(playerName[self]))
  
  # This function should print out every card that each player has

  # It begins by go

  for x in range(len(cardLoc)):

    if cardLoc[x] == self:

      print("{} of {}".format(rankName[x%13],suitName[int(x/13)]))

# The function should find out all the places where that number is in the deck

# It should the print out the rank and suit using the same modulus function

def main():

  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)          

main()