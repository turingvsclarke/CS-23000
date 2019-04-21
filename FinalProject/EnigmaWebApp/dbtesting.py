import sqlite3
from Enigma import*
import pdb

# We are going to create three tables. One of them stores the Enigma name and its id, one stores the rotors and their ids, the last one bridges between them
# This file is going to handle all the functions for adding and

# Create a rotor and enigma table

enigmaDB = sqlite3.connect("enigmas.db")

# This sets the cursur so that it will select individual items within a row
enigmaDB.row_factory = sqlite3.Row
c = enigmaDB.cursor()
# get the name of the machine and the plaintext using a bottle request

enigma_title = "enigma1"
plaintext = "egg salad sandwich"
state = 4
result = c.execute("""SELECT * FROM enigmas""").fetchone()
print(result)
# We need our array of rotors to be able to properly initiate our Enigma object
# Find the id of that machine's name
#pdb.set_trace()
enigma_id = c.execute("SELECT id FROM enigmas WHERE name = ?", (enigma_title,)).fetchone()
print(enigma_id)
'''reflector = c.execute("SELECT * FROM enigmas WHERE id = ?", (enigma_id,))
reflector = reflector['reflector']

# Create a list of all the rotor ids corresponding to that enigma id from the enigma_rotors table
result = c.execute("SELECT * FROM enigma_rotors WHERE enigma_id = ?", (enigma_id,))

rotors = []
for x in result:

    # get the rotor id
    rotor_id = int(x)    

    # get the rotor value at that id
    rotor = c.execute("SELECT value FROM rotors WHERE id = ?",(rotor_id)).fetchone()

    rotors.append(rotor)
# For each of those rotor ids we need to get their value and append them to a rotors array

# We need to find the correct machine, its correct rotors, and encrypt that

enigma = Enigma(state,rotors,reflector)

encryption = encrypt(plaintext,enigma)

print(encryption)'''