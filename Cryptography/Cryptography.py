# Create a program that encode a string of letters into a scrambled up string

# Create some sort of key string that will map one letter of the alphabet to a new letter

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Create a main function that looks exactly like Andy's function 

def main():

  keepGoing = True


  while keepGoing:


    response = menu()



    if response == "1":



      plain = input("text to be encoded: ")
      
      
      
      print(encode(plain))



    elif response == "2":



      coded = input("code to be decyphered: ")
   
   
   
      print (decode(coded))



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

    bad_input = True

    while bad_input:

        try:

            option_number = input("Please enter the number of what you would like to do.\n")

            bad_input = False

        except ValueError:

            print("That's not a valid option.")

            bad_input = True

    return(option_number)

# Create a function that encodes a string. It will take each value of that string, find it's index in the alphabet string, then return the value of the character in the key string

def encode(self):

    plain_text = self.upper()
    
    cipher = ""

    for x in plain_text:

        if x in key:

            index = key.index(x)

            cipher = cipher + alphabet[index]

    return(cipher)

# Create a function that decrypts a string. It will take each value of that string, find the index of that value in the key string, and return the value at that index in the alphabet string

def decode(self):

    cipher = self.upper()

    plain_text = ""

    for x in cipher:

        if x in key:

            index = alphabet.index(x)

            plain_text = plain_text + key[index]

    return(plain_text)

main()
