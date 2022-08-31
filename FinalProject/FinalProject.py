import random
import pdb

alphabet = "abcdefghijklmnopqrstuvwxyz"

# We are going to have a class that describes the current overall state of the Enigma machine and its size. This number will determine the states 
# of the individual rotors
class Enigma():

    def __init__ (self,state = 0, size = 0):
        object.__init__(self)
        self.setState(state)
        self.setSize(size)

    def setState(self,state):
        self._state = state

    def getState(self):
        return self._state

    # Making state a property so that it can be accessed by the Rotor
    state = property(fget = getState, fset = setState)

    def setSize(self,size):
        self._size = size

    def getSize(self):
        return self._size

    def getRotors(self):

        Rotors = []
        for i in range(self.getSize()):
            # For the ith rotor we have a state of 0, a position of i, and a new rotor string is generated each time
            rotor = createRotor()
            Rotors.append(Rotor(i,rotor))

        return Rotors

    # Since our rotor state depends upon the Enigma state, we update the rotors of the Enigma through the Enigma class, using a getState method in the
    # Rotor object
    def updateRotors(self):
        #pdb.set_trace()
        for i in range(self.getSize()):
            # For the ith rotor we update the state
            self.getRotors()[i].getState(self.getState())
        
    # A rotation (really of the first rotor but amounts to the same thing) is really just an addition to the overall Enigma state
    def Rotate(self,rotations):

        self.setState(self.getState()+rotations)

    def getRotorKey(self,rotor_number):

        key = self.getRotors()[rotor_number].getKey(self.getState())
        return key
          

class Rotor():
    # This is my class of rotor objects. It has three attributes: state, position, and rotor (the string of letters defining it)
    # Let's initialize the object. Note that its not passed a state because it doesn't really have its own state. Its state is dependent upon 
    # the state of the Enigma
    def __init__ (self,position = 0,rotor = []):
            object.__init__(self)
            self.setPosition(position)
            self.setrotor(rotor)

    # Each state is determined by the overall state of the Enigma and its position. Each state is whole divisor of the Enigma state when divided by 26^position
    def getState(self,state):
        return ((state%(26**(self.getPosition()+1)))//(26**self.getPosition()))

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position

    def setrotor(self,rotor):
        self._rotor = rotor

    def getrotor(self):
        return self._rotor

    def getKey(self,state):

        # We chop off the first state letters (1st state=only one letter) and put it at the front of the string
        return self.getrotor()[(26-state):26] + self.getrotor()[0:(26-state)]
          

    # Each rotor is going to be used as a key, which is determined by its rotor string and its state.
      
# For each rotor, we need to have a state. These states will change each time we call the rotateRotor method. The state will be a number from 0 through 25 indicating how many 
# letters the rotor has rotated through. The state at each point should be changed from x to (x+1)%26. 
# When a rotor's state reaches 0 (after rotation), it will switch the state of the rotor to the left (rotor r+1). This will continue for however many rotors we have.

# Each rotor will also need to have a position attribute, 0 through n. This should be immutable.

# Take input from the user

def createRotor():

    # Take each letter in the alphabet and randomly generate a new collection of these letters. This collection will be an iterable string.
    newrotor = ""
    global alphabet

    # Store the alphabet string locally so that we don't destroy the global variable for future use
    alphabet1 = alphabet

    while len(alphabet1)>0:

        index = random.randint(0,len(alphabet1)-1)
        letter = alphabet1[index]
        newrotor = newrotor + letter

        alphabet1 = alphabet1.replace(letter,"")
    
    return newrotor

def encrypt(message,enigma):
    # Initialize an empty string that will eventually hold the fully encrypted text
    encryption = ""
    global alphabet

    # store the alphabet string locally so that way we don't destroy it for future use
    alphabet1 = alphabet

    # Iterate through each message, encrypting one letter at a time
    for x in range(len(message)):

        letter = message[x]
        # For each letter, we loop through the cryptography encryption function r times, r being the number of rotors, passing it the current
        # rotor key and the new encryption message, which switches each time. At the end of the for loop we should have the correct letter
        
        rotors = enigma.getRotors()

        for y in range(len(enigma.getRotors())):
            # Find the letter's place in the alphabet
            index = alphabet.index(letter)
            # Assign the letter to the value of the xth rotor key at that index and then start over. Each time its then encrypting an encryption
            #pdb.set_trace()
            key = enigma.getRotorKey(y)

            letter = key[index]

        encryption = encryption + letter

        # Rotate the Enigma after each letter has been translated
        enigma.Rotate(1)
        enigma.updateRotors()

    return encryption
        
def main():

    keepgoing = True

    while keepgoing:

        message = input("Plaintext: ")
        numberofRotors = int(input("Number of Rotors: "))
        # Create a new Enigma machine
        enigma = Enigma(0,numberofRotors)

        # Create however many rotors the user wanted 
        # encrypt the message

        encryption = encrypt(message,enigma)
        print(encryption)
# create as many rotors as we need
# We need to be able to initiate an object for each of these rotors. That's tough.

# Assuming we have all these rotors, we now look at rotor number 26 at the
 
if __name__=="__main__":

    main()
