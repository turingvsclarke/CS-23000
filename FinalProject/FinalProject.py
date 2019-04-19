import random
import pdb

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Rotor():

    # This is my class of rotor objects. It has three attributes: state, position, and rotor (the string of letters defining it)

    # Let's initialize the class
    def __init__ (self,state = 0,position = 0,rotor = []):
            object.__init__(self)
            self.setState(state)
            self.setPosition(position)
            self.setrotor(rotor)

    def setState(self, state):
        self._state = state

    def getState(self):
        return self._state

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position

    def setrotor(self,rotor):
        self._rotor = rotor

    def getrotor(self):
        return self._rotor

    def rotateRotor(self,rotations):

        for x in range(rotations):

            # Put the last letter of the rotor's string at the first position of the list, then cut the list down to no longer include its last letter
            self.setrotor(self.getrotor()[25]+self.getrotor()[0:25])

            # Each time you rotate the rotor, change its state to be at a new number, making sure it loops back after passing through 26 states
            self.setState((self.getState() + 1)%26)

            # Each time you print out a new letter, check to see if the rotor has made a full revolution. If it has, rotate the next one, and so on.
            dontStop = True
            i = 0


            
# For each rotor, we need to have a state. These states will change each time we call the rotateRotor method. The state will be a number from 0 through 25 indicating how many 
# letters the rotor has rotated through. The state at each point should be changed from x to (x+1)%26. 
# When a rotor's state reaches 0 (after rotation), it will switch the state of the rotor to the left (rotor r+1). This will continue for however many rotors we have.

# Each rotor will also need to have a position attribute, 0 through n. This should be immutable.

# Take input from the user

def createRotor():

    # Take each letter in the alphabet and randomly generate a new collection of these letters. This collection will be an iterable string.
    newrotor = ""
    global alphabet
    alphabet1 = alphabet

    while len(alphabet1)>0:

        index = random.randint(0,len(alphabet1)-1)
        letter = alphabet1[index]
        newrotor = newrotor + letter

        alphabet1 = alphabet1.replace(letter,"")
    
    return newrotor

def encrypt(message,Rotors):
    # Initialize an empty string that will eventually hold the fully encrypted text
    encryption = ""
    global alphabet
    alphabet1 = alphabet
    # Iterate through each message, encrypting one letter at a time
    for x in range(len(message)):
        #pdb.set_trace()
        # Find the letter's place in the alphabet
        index = alphabet1.index(message[x])

        # The encrypted letter will be the corresponding entry of the last rotor
        encryption = encryption + Rotors[len(Rotors)-1].getrotor()[index]

        # Rotate the first rotor to the next letter
        Rotors[0].rotateRotor(1)  
    return encryption
        
def main():

    keepgoing = True

    while keepgoing:
        Rotors = []
        message = input("Plaintext: ")
        numberofRotors = int(input("Number of Rotors: "))
        # Create however many rotors the user wanted 

        for i in range(numberofRotors):
            # For the ith rotor we have a state of 0, a position of i, and a new rotor string is generated each time
            rotor = createRotor()
            Rotors.append(Rotor(0,i,rotor))
        # encrypt the message

        encryption = encrypt(message,Rotors)
        print(encryption)
# create as many rotors as we need
# We need to be able to initiate an object for each of these rotors. That's tough.

# Assuming we have all these rotors, we now look at rotor number 26 at the
 
if __name__=="__main__":

    main()
