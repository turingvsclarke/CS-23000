# Create a program that encode a string of letters into a scrambled up string

import random
import time

# Create some sort of key string that will map one letter of the alphabet to a new letter

# Create a main function that looks exactly like Andy's function 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

  default_key = "XPMGTDHLYONZBWEARKJUFSCIQV"

  keepGoing = True

  while keepGoing:

    response, key_decision = menu()

    if key_decision == "y":

      # Generate a new key and set it as the new default key

      key = key_generator(alphabet)

      default_key = key

    else:

      key = default_key

    if response == "1":

      plain = input("Text to be encoded: ")
      
      print(encode(plain,key))

    elif response == "2":

      coded = input("Code to be decyphered: ")
   
      print (decode(coded,key))

    elif response == "0":

      print ("Thanks for doing secret spy stuff with me.")
     
      keepGoing = False
    
    else:
      print ("I don't know what you want to do...")

# Create a menu function that prints out the various options, mainly encryption, decryption, and quitting the program

def menu():

    option_numbers = ["0)","1)","2)"]

    options = ["Quit","Encode","Decode"]

    for x in options:

        print("{:<4}{:>8}".format(option_numbers[options.index(x)],x))

    option_number = input("Please enter the number of what you would like to do.\n")

    key_decision = input("Would you like to generate a new key(y)? Otherwise the previous key will be used.\n")

    return(option_number,key_decision)

# Create a function that encodes a string. It will take each value of that string, find it's index in the alphabet string, then return the value of the character in the key string

def encode(self,key):

    plain_text = self.upper()
    
    cipher = ""

    for x in plain_text:

        if x in key:

            index = key.index(x)

            cipher = cipher + alphabet[index]

    return(cipher)

# Create a function that decrypts a string. It will take each value of that string, find the index of that value in the key string, and return the value at that index in the alphabet string

def decode(self,key):

    cipher = self.upper()

    plain_text = ""

    for x in cipher:

        if x in key:

            index = alphabet.index(x)

            plain_text = plain_text + key[index]

    return(plain_text)

def key_generator(self):

    # Create a while loop that will continue as long as the length of the decreasing alphabet string is greater than 0

    key = ""

    while len(self)>0:

    # Generate a random number between 0 and the length of the alphabet string - 1

        index = random.randint(0,len(self)-1)

    # Take the letter at the index of that random number and append it to the key string

        key = key + self[index]

    # Make the alphabet string itself with the letter we just used removed

        self = self.replace(self[index],"")

    print("Here's the key I'm going to use: ")
    print(key)

    return(key)

main()